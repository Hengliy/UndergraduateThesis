// pages/join/join.js
const app = getApp()
const cookieUtil = require('../../../utils/cookie.js')
const authUtil = require('../../../utils/auth.js')

Page({

  /**
   * 页面的初始数据
   */
  data: {
    groupBriefList:[]
  },

  getAllGroupBrief: function(){
    var that = this
    var newCookie = cookieUtil.getCookieFromStorage()//拿出cookie
    var header = {}
    header.Cookie = newCookie

    wx.request({
      url: app.globalData.serverUrl+'/group/getAllGroupBrief',
      method:'GET',
      header:header,
      success: function (res) {
        if(res.statusCode == 200)
        {
          console.log(res)
          let str = "groupBriefList"
          that.setData({
            [str]: res.data.data
          })
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getAllGroupBrief()
    console.log(this.data.groupBriefList)
  },

  gotoDetails: function(e){
    console.log("join matchid=" + e.currentTarget.dataset.matchid)
    wx.navigateTo({
      url: '../groupDetail/groupDetail?groupId=' + e.currentTarget.dataset.matchid
    })
  },

  addNewGroup: function(e){
    wx.navigateTo({
      url: '../addNewGroup/addNewGroup',
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