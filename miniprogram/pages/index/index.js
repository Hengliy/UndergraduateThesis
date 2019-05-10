//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    motto: 'Hello World',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },
  //事件处理函数
  bindViewTap: function () {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad: function () {
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo,
        hasUserInfo: true
      })
    } else if (this.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          app.globalData.userInfo = res.userInfo
          this.setData({
            userInfo: res.userInfo,
            hasUserInfo: true
          })
        }
      })
    }
  },
  getUserInfo: function (e) {
    console.log(e)
    app.globalData.userInfo = e.detail.userInfo
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },

  //////////////////////////////////////////////////////////////////////////////////////
  name: function (e) {   //获取input输入的值
    var that = this;
    that.setData({
      name: e.detail.value
    })
  },
  ID_num: function (e) {    //获取input输入的值
    var that = this;
    that.setData({
      ID_num: e.detail.value
    })
    var id_num = that.data.ID_num
    if (!(id_num.length === 15 || id_num.length === 18)) {
      wx.showToast({
        title: '请输入15或18位数身份证号码',
        image: '../Image/error.png',
        duration: 2000
      })
    }
  },

  formSubmit: function (e) {
    var that = this;
    var tokend = wx.getStorageSync('tokend')
    var name2 = e.detail.value.name2;         //获取input初始值
    var ID_num2 = e.detail.value.ID_num2;    //获取input初始值
    var name = that.data.name ? that.data.name : name2    //三元运算，如果用户没修改信息，直接提交原来的信息，如果用户修改了信息，就将修改了的信息和未修改过的信息一起提交
    var ID_num = that.data.ID_num ? that.data.ID_num : ID_num2
    wx.request({
      method: 'POST',
      url: 'https://....?token=' + tokend, //接口地址
      data: {
        'name': name,
        'ID_num': ID_num
      },
      header: { 'content-type': 'application/json' },
      success: function (res) {
        wx.showToast({
          title: '资料修改成功',
          image: '../Image/suess.png',
          duration: 2000
        })
        setTimeout(function () {
          wx.switchTab({
            url: '../index/index',
          })
        }, 2000)

      },
      fail: function (res) {
        console.log('cuowu' + ':' + res)
      }
    })
  }

})
