// pages/join/join.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    contestTypeList:[],
    contestInfoList:[]
  },

  getAllContestType: function(){
    header={}
    wx.request({
      url: app.global.serverurl+'/contest/getAllContestType',
      method:'GET',
      success: function (res) {
        if(res.statusCode == 200)
        {
          console.log(res.data)
          wx.showModal({
            title: '注册成功！',
            content: '请等待管理员审核，审核之后即可登陆会员中心',
          })
        }
      }
    })
  },

  getAllContestInfo: function () {
    header = {}
    wx.request({
      url: app.global.serverurl + '/contest/getAllContestInfo',
      method: 'GET',
      success: function (res) {
        if (res.statusCode == 200) {
          console.log(res.data)
          wx.showModal({
            title: '注册成功！',
            content: '请等待管理员审核，审核之后即可登陆会员中心',
          })
        }
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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