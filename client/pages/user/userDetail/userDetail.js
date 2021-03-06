// pages/userDetail/userDetail.js

const app = getApp()
const cookieUtil = require('../../../utils/cookie.js')
const authUtil = require('../../../utils/auth.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    userData: {},
    hasUserData: false,
    
    sexList:['男','女'],//角色选择
    sexPickIndex:0,

    dutyList:[],
    dutyInfo:[],
    dutyPickIndex: 0,

    departmentPickIndex0: 0,
    departmentList0:[],

    departmentPickIndex1: 0,
    departmentList1:[],
    departmentList1Pick:[],

    departmentPickIndex2: 0,
    departmentList2:[],
    departmentList2Pick:[]
  },

  getDepartmentList: function(parentIndex,theLevel)
  {
    var that=this
    wx.request({
      url: app.globalData.serverUrl +'/department/getDepartmentList?parentIndex='+parentIndex+'&theLevel='+theLevel,
      method:"GET",
      success: function(res){
        if(res.statusCode==200)
        {
          if (theLevel == 1) {
            let str = "departmentList0"
            that.setData({
              [str]: res.data.data,
            })
          } else if (theLevel == 2) {
            let str = "departmentList1"
            that.setData({
              [str]: res.data.data,
            })
          } else if (theLevel == 3) {
            let str = "departmentList2"
            that.setData({
              [str]: res.data.data,
            })
          }

          console.log("departmentList0 = ",that.data.departmentList0)
          console.log("departmentList1 = ",that.data.departmentList1)
          console.log("departmentList2 = ",that.data.departmentList2)
        }
      }
    })
  },

  getDutyList: function () {
    var that = this
    wx.request({
      url: app.globalData.serverUrl + '/app01/getDutyList',
      method: "GET",
      success: function (res) {
        if (res.statusCode == 200) {

          let str="dutyInfo"
          that.setData({
            [str]:res.data.data
          })

          console.log(that.data.dutyInfo)
          console.log(that.data.sexList)
        }
      }
    })
  },

  getUserData: function()
  {
    var that = this
    var newCookie = cookieUtil.getCookieFromStorage()//拿出cookie
    var header = {}
    header.Cookie = newCookie

    wx.request({
      url: app.globalData.serverUrl + '/user/getUserData',
      header: header,
      method: "GET",
      success: function (res) {
        if (res.statusCode == 200) {
          console.log(res.data)
          app.globalData.userData = res.data.data[0]
          that.setData({
            userData: res.data.data[0],
            dutyPickIndex: res.data.data[0]["useridutyiid_id"],
            //departmentPickIndex2: res.data.data[0]["useridepartmentiid_id"],
            hasUserData: true
          })

          //注意！对data{}的每次修改都要在setData中进行
          if (that.data.userData["userisex"] == that.data.sexList[0]) {
            that.setData({
              sexPickIndex: 0
            })
          } else {
            that.setData({
              sexPickIndex: 1
            })
          }
        }
        console.log("userData = ", app.globalData.userData)
        console.log("dutyPickIndex = " + that.data.dutyPickIndex)
        console.log("sexPickIndex = " + that.data.sexPickIndex)
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
   
    this.getUserData()
    this.getDutyList()
    this.getDepartmentList(-1, 1)
    console.log("that.data.departmentList0 = ",this.data.departmentList0)
    //如果要下面显示，那么就要考虑异步处理，就要promise函数
    // that.getDepartmentList(departmentList0[departmentPickIndex0]["id"], 2)
    // that.getDepartmentList(departmentList1[departmentPickIndex1]["id"], 3)
  },

  formSubmit:function(e){
    var header = { "content-type": "application/json"}		//使用POST方法要带上这个header}
    var cookie=cookieUtil.getCookieFromStorage()
    header.Cookie=cookie
    var that =this
    console.log(e.detail.value)
    console.log(cookie)

    wx.request({
      url: app.globalData.serverUrl+'/user/updateUserData',
      method:'PUT',
      data:e.detail.value,
      header:header,
      success:function(res){
        console.log(res)
        wx.showModal({
          title: '保存成功',
          content: '',
        })
      }
    })
  },

  dutyPickerChange : function(e)
  {
    console.log("修改用户数据，picker选择duty为"+e.detail.value)
    this.setData({
      dutyPickIndex:e.detail.value
    })
  },

  sexPickerChange: function(e)
  {
    console.log("修改用户数据，picker选择sex为" + e.detail.value)
    this.setData({
      sexPickIndex: e.detail.value
    })
  },

  departmentPickerChange: function (e) {
    if(e.currentTarget.id=="depart0"){
      this.setData({
        departmentPickIndex0: e.detail.value
      })
      this.getDepartmentList(this.data.departmentList0[this.data.departmentPickIndex0]["id"], 2)
    } else if (e.currentTarget.id == "depart1") {
      this.setData({
        departmentPickIndex1: e.detail.value        
      })
      this.getDepartmentList(this.data.departmentList1[this.data.departmentPickIndex1]["id"], 3)
    }
    else if (e.currentTarget.id == "depart2") {
      this.setData({
        departmentPickIndex2: e.detail.value      
      })

      var name = this.data.departmentList0[this.data.departmentPickIndex0]["name"] + this.data.departmentList1[this.data.departmentPickIndex1]["name"] + this.data.departmentList2[this.data.departmentPickIndex2]["name"]
      this.setData({
        wholedepartmentname: name
      })
    }
    console.log(this.data.departmentPickIndex0,this.data.departmentPickIndex1,this.data.departmentPickIndex2)
  },

  usericodeChange: function (e) {
    console.log("*****************" + e.detail.value)
    console.log(app.globalData.serverUrl + '/user/isExist?usericode=' + e.detail.value)
    wx.request({
      url: app.globalData.serverUrl + '/user/isExist?usericode=' + e.detail.value,
      method: 'GET',
      success: function (res) {
        if (res.data.result_code == app.globalData.FAILED) {
          wx.showModal({
            title: '账号冲突，请换一个账号',
            content: '',
          })
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})