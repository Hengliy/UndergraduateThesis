// pages/contest/contest.js
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    contestTypeList: [],
    contestInfoList: []
  },

  getAllContestType: function (parentindex) {
    var that=this
    wx.request({
      url: app.globalData.serverUrl + '/contest/getContestListByParentindex?parentindex='+parentindex,
      method: 'GET',
      success: function (res) {
        if (res.statusCode == 200) {

          let str = "contestTypeList"
          that.setData({
            [str]: res.data.data
          })

          console.log(res.data)
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
    var that=this
    // if (!app.globalData.jwt) {
    //   wx.redirectTo({
    //     url: '../login/login',
    //   })
    //   return false
    // }
    that.getAllContestType(-1)
  },

  //进入活动详情
  gotoDetails: function(e) {
    const matchId = e.currentTarget.dataset.matchid
    // app.globalData.contestParentIndex=matchId
    console.log("go to detail")
    wx.navigateTo({
      url: '../contest/contestsub1/contestsub1?parentindex='+matchId
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