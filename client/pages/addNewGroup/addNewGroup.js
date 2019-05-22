// pages/contest/contestDetail/contestDetail.js
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    contestInfo: null,
    index2: 0,
    sexs: [
      '  ', '男', '女', '其他'
    ],
    groupInfo: null,
    updateFlag: false
  },

  getGroupInfo: function (groupId) {
    var that = this
    wx.request({
      url: app.globalData.serverUrl + '/group/getGroupInfoById?ID=' + groupId,
      method: 'GET',
      success: function (res) {
        if (res.statusCode == 200) {
          that.setData({
            groupInfo: res.data.data[0]
          })
        }
        console.log(that.data.groupInfo)
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      updateFlag: true
    })
    this.getGroupInfo(options.groupId)
    console.log("groupInfo = ", this.data.groupInfo)
  },

  getSex: function (e) {
    this.setData({
      sex: this.data.sexs[Number.parseInt(e.detail.value, 10)],
      index2: e.detail.value
    });
  },

  updateGroupInfo: function (e) {
    this.setData({
      updateFlag: false
    })
  },

  saveGroupInfo: function (e) {
    var header = { "content-type": "application/json" }		//使用POST方法要带上这个header}
    var cookie = cookieUtil.getCookieFromStorage()
    header.Cookie = cookie
    var that = this
    console.log(e.detail.value)
    console.log(cookie)

    wx.request({
      url: app.globalData.serverUrl + '/group/updateGroupInfo',
      method: 'PUT',
      data: e.detail.value,
      header: header,
      success: function (res) {
        console.log(res)
        wx.showModal({
          title: '保存成功',
          content: '',
        })
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