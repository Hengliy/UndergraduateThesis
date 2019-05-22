// pages/menu/menu.js

const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {

    dutyID:null,

  },

  // onNavigatorTap: function (e) {
  //   var index = e.currentTarget.dataset.index
  //   console.log(index)
  //   if (index == 0) {
  //     wx.navigateTo({
  //       url: '../register/register',
  //     })
  //   } else if (index == 1) {
  //     wx.navigateTo({
  //       url: '../apply/apply',
  //     })
  //   } else if (index == 2) {
  //     wx.navigateTo({
  //       url: '../index/index'
  //     })
  //   } else if (index == 3) {
  //     wx.navigateTo({
  //       url: '../logs/logs'
  //     })
  //   } 
  // },



  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function(options) {
    console.log(app.globalData.userData)
    this.updateMenuData()
    console.log(this.data.dutyID)
  },

  /**
   * 请求后台，更新menu数据
   */
  updateMenuData: function() {
    this.setData({
      dutyID: app.globalData.userData["useridutyiid_id"]
    })
    // var that = this
    // wx.request({
    //   url: app.globalData.serverUrl + app.globalData.apiVersion + '/service/menu',
    //   success: function(res){
    //     var menuData = res.data.data
    //     that.setData({
    //       grids: menuData
    //     })
    //   }
    // })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function() {

  }
})