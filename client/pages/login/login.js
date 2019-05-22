const app = getApp()
const cookieUtil = require('../../utils/cookie.js')
const authUtil = require('../../utils/auth.js')

Page({
  data: {		//此处定义本页面中的全局变量
    result: '',
    username: '',
    passwd: '',
    hasMask: false,
    access: {
      title: "微信授权",
      msg: '获得你公开信息（昵称、头像）',
      cancle: '取消',
      confirm: '授权'
    }
  },


  //事件处理函数
  bindViewTap: function () {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },

  showMask: function () {
    this.setData({
      hasMask: true
    })
    console.log("show")
  },

  preventTouchMove: function (e) {
    console.log("preventTouchMove event: " + e)
  },

  tapcatch: function (e) {
    console.log("tapcatch event: " + e)
  },

  cancle: function () {
    this.setData({
      hasMask: false
    })
  },


  onLoad: function(opstions){
    if (app.globalData.jwt) {
      wx.switchTab({
        url: '../contest/contestList/contesList',
      })
    }
  },
  
  inputName: function (e) {	// 用于获取输入的账号
    this.setData({
      username: e.detail.value	//将获取到的账号赋值给username变量
    })
  },
  inputPwd: function (e) {		// 用于获取输入的密码
    this.setData({
      passwd: e.detail.value	//将获取到的账号赋值给passwd变量
    })
  },

  /**
  * 控制 pop 的打开关闭
  * 该方法作用有2:
  * 1：点击弹窗以外的位置可消失弹窗
  * 2：用到弹出或者关闭弹窗的业务逻辑时都可调用
  */
  register: function(e){
    wx.navigateTo({
      url: '../register/register'
    })
  },

  toggleDialog:function() {
    this.setData({
      showDialog: !this.data.showDialog
    })},

  getUserData: function () {
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
        }

        console.log("userData = ", app.globalData.userData)
      }
    })
  },

  login: function (e) {		//与服务器进行交互
  var that =this
    wx.request({
      url: 'http://127.0.0.1:8000/login/login',	//获取服务器地址，此处为本地地址
      header: {
        "content-type": "application/x-www-form-urlencoded"		//使用POST方法要带上这个header
      },
      method: "POST",
      data: {		//向服务器发送的信息
        // username: this.data.username,
        // passwd: this.data.passwd

        usericode: 'shilei333',
        passwd: 'QRxuC4I7poBegu/OyCNkvA=='
      },
      success: res => {
        if (res.data.result_code == app.globalData.SUCCESS) 
        {
          that.setData({
            result: res.data.message	//服务器返回的结果
          })

          var cookie = cookieUtil.getSessionIDFromResponse(res)
          console.log(cookie)
          cookieUtil.setCookieToStorage(cookie)

          that.getUserData()

          app.globalData.jwt=true

          
          
          console.log("跳转")
          wx.switchTab({
            // url: '/pages/user/user?username=' + '石雷'
            // url:'/pages/userDetail/userDetail'
            url: '/pages/contest/contestList/contestList?parentindex=-1'
          })

        }
        else if (res.data.result_code == app.globalData.FAILED)
        {
           this.setData({
            result: res.data.message	//服务器返回的结果
          })
        }
      }
    })
  }

})