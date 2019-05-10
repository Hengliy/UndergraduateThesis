const app = getApp()
const cookieUtil = require('../../utils/cookie.js')
const authUtil = require('../../utils/auth.js')

Page({
  data: {		//此处定义本页面中的全局变量
    result: '',
    username: '',
    passwd: ''
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

  register: function(e){
    wx.navigateTo({
      url: '../register/register'
    })
  },

  login: function (e) {		//与服务器进行交互
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
          this.setData({
            result: res.data.message	//服务器返回的结果
          })

          var cookie = cookieUtil.getSessionIDFromResponse(res)
          console.log(cookie)
          cookieUtil.setCookieToStorage(cookie)

          wx.navigateTo({
            // url: '/pages/user/user?username=' + '石雷'
            url:'/pages/userDetail/userDetail'
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