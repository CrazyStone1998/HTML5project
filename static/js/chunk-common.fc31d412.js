(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[1],{"3TiO":function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-row",{staticClass:"app-bar",attrs:{type:"flex",align:"middle"}},[n("el-col",{attrs:{span:6}},[n("router-link",{attrs:{to:"/"}},[n("el-button",{staticStyle:{"vertical-align":"middle",width:"3em"},attrs:{type:"text"}},[n("icon",{attrs:{src:e.backIcon}})],1)],1)],1),n("el-col",{staticClass:"title",attrs:{span:12}},[n("h1",[e._t("default")],2)]),n("el-col",{staticClass:"right",staticStyle:{"text-align":"right"},attrs:{span:6}},[e._t("right")],2)],1)},o=[],i=n("za7x"),a=n("Ba7Q"),s=n.n(a),u={name:"AppBar",components:{Icon:i["a"]},data:function(){return{backIcon:s.a}},methods:{}},c=u,l=(n("RBw5"),n("KHd+")),d=Object(l["a"])(c,r,o,!1,null,"6d3835c8",null);t["a"]=d.exports},"4LYi":function(e,t,n){e.exports=n.p+"img/login_back.518a2d54.png"},"7Qib":function(e,t,n){"use strict";n.d(t,"e",function(){return o}),n.d(t,"d",function(){return i}),n.d(t,"f",function(){return a}),n.d(t,"c",function(){return s}),n.d(t,"b",function(){return u}),n.d(t,"a",function(){return c});n("ls82");var r=n("MECJ"),o=(n("Oyvg"),n("pIFo"),function(e){return e.slice(0,1).toUpperCase().concat(e.slice(1))}),i=function(e){return e.slice(0,1).toLowerCase().concat(e.slice(1))};function a(e){return new Promise(function(t){setTimeout(function(){t()},e)})}function s(){return new Promise(function(e,t){AMap.plugin("AMap.Geolocation",function(){var n=new AMap.Geolocation({enableHighAccuracy:!0,GeoLocationFirst:!0});n.getCurrentPosition();var r=Date.now(),o=5,i=null;function a(t){(!i||t.accuracy<i.accuracy)&&(i=t),Date.now()-r<1e3*o?n.getCurrentPosition():e({lng:i.position.lng,lat:i.position.lat})}function s(e){console.log("定位失败  ".concat(Date.now()," ").concat(e)),t(e)}AMap.event.addListener(n,"complete",a),AMap.event.addListener(n,"error",s)})})}function u(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{width:500,height:500},n=e.width,r=e.height,o=n/r,i=t.width/t.height,a=o>i?t.width:t.height*o,s=o<i?t.height:t.width/o,u=document.createElement("canvas"),c=u.getContext("2d");return u.width=a,u.height=s,c.drawImage(e,0,0,a,s),new Promise(function(e){u.toBlob(function(t){var n=new File([t],"".concat(Date.now(),".jpg"));e(n)},"image/jpeg")})}function c(e){return l.apply(this,arguments)}function l(){return l=Object(r["a"])(regeneratorRuntime.mark(function e(t){var n,r,o,i,a=arguments;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return n=a.length>1&&void 0!==a[1]?a[1]:{},r=document.createElement("canvas"),o=n.boxConstraint,o=o?"boolean"===typeof o||o instanceof Boolean?{width:200,height:200}:{width:o.width,height:o.height}:{width:t.videoWidth,height:t.videoHeight},t.videoHeight/t.videoWidth>o.height/o.width?(r.height=o.height,r.width=r.height*t.videoWidth/t.videoHeight):(r.width=o.width,r.height=r.width*t.videoHeight/t.videoWidth),r.getContext("2d").drawImage(t,0,0,r.width,r.height),e.next=8,new Promise(function(e){return r.toBlob(function(t){e(t)},"image/jpeg")});case 8:return i=e.sent,e.abrupt("return",new File([i],"video_capture_".concat(Date.now()),{lastModified:Date.now()}));case 10:case"end":return e.stop()}},e,this)})),l.apply(this,arguments)}},Ba7Q:function(e,t){e.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAjCAYAAACU9ioYAAAA3klEQVRIia3WOwrDMAyA4T/tIbMFupVeIJm7tL1A6QkCPlFOE9pJkAZbkWRrtODDYOvRLctCZUzAA3illKauEhRM4nVqiAGMUTCHAcwRsIgBgxdUsZTS6gEPMQAraMKsoBmzgCoGrPuEBroxDQxhJTCM5cAqbA9WY1uwCSZgM0zAHLYCFy8m4CdzfgbuXkzAWwEdgWcE/LZE5ZWbodt/2ATdV0o1mqvlKrTUbcKo1g9D6FHHdqOWmaKifd//odapZ0Y9c9mERravDngD10wutH2pN41uXyU0tH2V0BkYfihlchvr/DBGAAAAAElFTkSuQmCC"},Eoag:function(e,t,n){},G5V7:function(e,t,n){},HWu3:function(e,t,n){"use strict";var r=n("Eoag"),o=n.n(r);o.a},J9k6:function(e,t,n){"use strict";n.d(t,"c",function(){return a}),n.d(t,"d",function(){return s}),n.d(t,"a",function(){return u}),n.d(t,"e",function(){return c}),n.d(t,"f",function(){return l}),n.d(t,"g",function(){return d}),n.d(t,"b",function(){return f});n("91GP");var r=n("dRp0"),o=n("Qyje"),i=n.n(o);function a(e){return r["b"].get("group",{params:{id:e}}).then(r["a"])}function s(){return r["b"].get("group/list").then(r["a"])}function u(e){return r["b"].post("group/add",i.a.stringify({name:e})).then(r["a"])}function c(e){return r["b"].post("group/join",i.a.stringify({id:e})).then(r["a"])}function l(e){return r["b"].post("group/quit",i.a.stringify({id:e})).then(r["a"])}function d(e,t){return r["b"].post("group/update",i.a.stringify(Object.assign({id:e},t))).then(r["a"])}function f(e){return r["b"].post("group/delete",i.a.stringify({id:e})).then(r["a"])}},NJ9t:function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-container",{attrs:{id:"RfContainer"}},[n("el-form",{ref:"ruleForm",staticStyle:{width:"80%",margin:"0 auto"},attrs:{"status-icon":"",model:e.ruleForm,rules:e.rules}},[n("el-form-item",{attrs:{label:"用户名",prop:"username"}},[n("el-input",{attrs:{type:"text"},model:{value:e.ruleForm.username,callback:function(t){e.$set(e.ruleForm,"username",t)},expression:"ruleForm.username"}})],1),n("el-form-item",{attrs:{label:"密码",prop:"password"}},[n("el-input",{attrs:{type:"password"},model:{value:e.ruleForm.password,callback:function(t){e.$set(e.ruleForm,"password",t)},expression:"ruleForm.password"}})],1),n("el-form-item",{attrs:{label:"确认密码",prop:"checkpassword"}},[n("el-input",{attrs:{type:"password"},model:{value:e.ruleForm.checkpassword,callback:function(t){e.$set(e.ruleForm,"checkpassword",t)},expression:"ruleForm.checkpassword"}})],1),n("el-form-item",{attrs:{label:"用户类型",prop:"userType"}},[n("br"),n("el-select",{attrs:{placeholder:"请选择用户类型"},model:{value:e.ruleForm.userType,callback:function(t){e.$set(e.ruleForm,"userType",t)},expression:"ruleForm.userType"}},[n("el-option",{attrs:{label:"签到端用户",value:0}}),n("el-option",{attrs:{label:"管理端用户",value:1}})],1)],1),n("el-form-item",{attrs:{label:"姓名",prop:"name"}},[n("el-input",{model:{value:e.ruleForm.name,callback:function(t){e.$set(e.ruleForm,"name",t)},expression:"ruleForm.name"}})],1),n("el-form-item",{attrs:{label:"本人照片",prop:"profile"}},[n("el-upload",{staticClass:"upload-demo",attrs:{drag:"",action:"","on-change":e.getFile,"on-preview":e.handlePreview,"on-remove":e.handleRemove,"before-remove":e.beforeRemove,"on-exceed":e.handleExceed,limit:1,"auto-upload":!1}},[n("i",{staticClass:"el-icon-upload"}),n("div",{staticClass:"el-upload__text"},[e._v("将文件拖到此处，或"),n("em",[e._v("点击上传")])])])],1),n("el-form-item",[n("el-button",{staticStyle:{width:"100%"},attrs:{type:"primary"},on:{click:function(t){e.submitForm("ruleForm")}}},[e._v("注册")])],1)],1)],1)},o=[],i=(n("f3/d"),n("RW0V"),n("rGqo"),n("ssfR")),a=n("7Qib"),s={name:"RegisterForm",created:function(){/Android|webOS|iPhone|iPod|BlackBerry/i.test(navigator.userAgent)?this.pcOrPhone=!1:this.pcOrPhone=!0},mounted:function(){},data:function(){var e=this,t=function(e,t,n){if(!t)return n(new Error("账号不能为空"));setTimeout(function(){n()},100)},n=function(t,n,r){""===n?r(new Error("请输入密码")):(""!==e.ruleForm.checkpassword&&e.$refs.ruleForm.validateField("checkpassword"),r())},r=function(t,n,r){""===n?r(new Error("请再次输入密码")):n!==e.ruleForm.password?r(new Error("两次输入密码不一致!")):r()},o=function(e,t,n){if(!t)return n(new Error("请上传正脸照片"));setTimeout(function(){n()},100)},i=function(e,t,n){if(!t)return n(new Error("请拍照"));setTimeout(function(){n()},100)};return{ruleForm:{username:"",password:"",checkpassword:"",name:"",userType:null,profile:!1,pcOrPhone:!0,photo_PC:null},rules:{username:[{required:!0,validator:t,trigger:"blur"}],password:[{required:!0,validator:n,trigger:"blur"}],checkpassword:[{required:!0,validator:r,trigger:"blur"}],name:[{required:!0,message:"请输入姓名",trigger:"blur"}],userType:[{required:!0,message:"请选择用户类型",trigger:"blur"}],profile:[{required:!0,validator:o,trigger:"blur"}],photo_PC:[{required:!0,validator:i,trigger:"blur"}]}}},computed:{ruleFormData:function(){var e=this,t=new FormData;return console.log(this.ruleForm),Object.keys(this.ruleForm).forEach(function(n){"checkpassword"!==n&&t.append(n,e.ruleForm[n])}),console.log(t),t}},methods:{getFile:function(e,t){this.ruleForm.profile=e.raw},submitForm:function(e){var t=this;this.$refs[e].validate(function(e){if(!e)return console.log("error submit!!"),!1;new Promise(function(e){var n=t.ruleFormData,r=new Image;r.src=URL.createObjectURL(n.get("profile")),r.onload=function(){Object(a["b"])(r).then(function(t){n.append("profile",t),e(n)})}}).then(function(e){return Object(i["d"])(e)}).then(function(){t.$message({message:"注册成功  正在跳转",type:"success"}),setTimeout(function(){t.$router.push("/login")},2e3)},function(e){t.$message.error("出错：".concat(e.message))})})},resetForm:function(e){this.$refs[e].resetFields()},handleRemove:function(e,t){console.log(e,t),this.fileList=[]},handlePreview:function(e){console.log(e)},handleExceed:function(e,t){this.$message.warning("当前限制选择 1 个文件")},beforeRemove:function(e,t){return this.$confirm("确定移除 ".concat(e.name,"？"))}}},u=s,c=(n("Rqe1"),n("HWu3"),n("KHd+")),l=Object(c["a"])(u,r,o,!1,null,"f0442886",null);t["a"]=l.exports},RBw5:function(e,t,n){"use strict";var r=n("gAeg"),o=n.n(r);o.a},RPjt:function(e,t,n){"use strict";var r=n("G5V7"),o=n.n(r);o.a},Rqe1:function(e,t,n){"use strict";var r=n("qt8B"),o=n.n(r);o.a},VOVZ:function(e,t,n){"use strict";n.d(t,"d",function(){return o}),n.d(t,"b",function(){return i}),n.d(t,"a",function(){return a}),n.d(t,"c",function(){return s});var r=n("dRp0");n("Qyje");function o(e,t){return r["b"].get("group/"+e+"/user/"+t).then(r["a"])}function i(e){return r["b"].get("history/"+e).then(r["a"])}function a(e){return r["b"].get("group/"+e+"/user/record").then(r["a"])}function s(e){return r["b"].get("record/"+e).then(r["a"])}},YN8A:function(e,t,n){"use strict";var r=n("k4UR"),o=n.n(r);o.a},YbHW:function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-form",{ref:"form",attrs:{model:e.form,rules:e.rules}},[n("el-form-item",{attrs:{label:"账号",prop:"username"}},[n("el-input",{attrs:{type:"text"},model:{value:e.form.username,callback:function(t){e.$set(e.form,"username",t)},expression:"form.username"}})],1),n("el-form-item",{attrs:{label:"密码",prop:"password"}},[n("el-input",{attrs:{type:"password"},model:{value:e.form.password,callback:function(t){e.$set(e.form,"password",t)},expression:"form.password"}})],1),n("el-form-item",[n("el-button",{staticStyle:{width:"100%"},attrs:{type:"primary",disabled:e.submitting},on:{click:e.submit}},[n("i",{class:[e.submitting?"el-icon-loading":""]}),e._v(e._s(e.submitting?"":"登录")+"\n        ")])],1)],1)},o=[],i=(n("ls82"),n("MECJ")),a=n("ssfR"),s=n("7Qib"),u={name:"LoginForm",props:{redirect:{type:String}},data:function(){return{form:{username:"",password:""},rules:{username:[{required:!0,message:"请输入用户名"}],password:[{required:!0,message:"请输入密码"}]},submitting:!1}},methods:{submit:function(){var e=Object(i["a"])(regeneratorRuntime.mark(function e(){var t,n;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return this.submitting=!0,e.prev=1,e.next=4,Object(a["b"])(this.form.username,this.form.password);case 4:return t=e.sent,this.$message({message:"登陆成功  正在跳转",type:"success"}),e.next=8,Object(s["f"])(2e3);case 8:this.redirect?window.location.href=this.redirect:(n=0===t.userType?"user":"management",window.location.href="/".concat(n,".html")),e.next=14;break;case 11:e.prev=11,e.t0=e["catch"](1),this.$message.error("出错：".concat(e.t0.message));case 14:return e.prev=14,this.submitting=!1,e.finish(14);case 17:case"end":return e.stop()}},e,this,[[1,11,14,17]])}));return function(){return e.apply(this,arguments)}}()}},c=u,l=(n("xhDR"),n("KHd+")),d=Object(l["a"])(c,r,o,!1,null,"ff32427c",null);t["a"]=d.exports},cRnl:function(e,t,n){"use strict";n.d(t,"b",function(){return a}),n.d(t,"a",function(){return s}),n.d(t,"c",function(){return u}),n.d(t,"d",function(){return c});n("91GP");var r=n("dRp0"),o=n("Qyje"),i=n.n(o);function a(e){return r["b"].get("leave",{params:{group_id:e}}).then(r["a"])}function s(e){return r["b"].get("leave/".concat(e,"/feedback")).then(r["a"])}function u(e,t){var n=new FormData;return n.set("result",t),n.set("group_id",e),r["b"].post("group/leave",n).then(r["a"])}function c(e){return r["b"].post("leave/response",i.a.stringify(Object.assign(e))).then(r["a"])}},dRp0:function(e,t,n){"use strict";n.d(t,"b",function(){return d}),n.d(t,"a",function(){return m});var r=n("xmWZ"),o=n("3Aqn"),i=n("0yhX"),a=n("EdlT"),s=n("4A8Y"),u=n("vDqi"),c=n.n(u),l="/api/v1",d=c.a.create({baseURL:l});d.interceptors.request.use(function(e){return e.params=e.params||{},e.params.t=Date.now(),e});var f=function(e){function t(e,n){var o;return Object(r["a"])(this,t),o=Object(i["a"])(this,Object(a["a"])(t).call(this)),o.message=e,o.status=n,o}return Object(o["a"])(t,e),t}(Object(s["a"])(Error)),m=function(e){var t=e.data;if(200===t.status)return t.data;throw new f(e.data.message,e.data.status)}},gAeg:function(e,t,n){},k4UR:function(e,t,n){},mDl2:function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[n("div",{style:e.note,attrs:{id:"headOut"}},[n("div",{staticStyle:{height:"45px",width:"45px","background-color":"#00ffff00",display:"inline-block",position:"absolute",top:"50%",transform:"translate(0, -50%)","border-radius":"25px","margin-left":"5%"},attrs:{id:"headphoto"},on:{click:function(t){e.showEditPerInfo()}}}),n("div",{staticStyle:{right:"0",height:"60%",position:"absolute",top:"50%",transform:"translate(0, -50%)","margin-right":"5%"},attrs:{id:"headIn"}},[n("el-button",{staticStyle:{color:"white"},attrs:{type:"text"},on:{click:e.logoutFunction}},[e._v("注销账户")])],1)]),n("el-dialog",{attrs:{title:"个人信息",visible:e.dialogFormVisible},on:{"update:visible":function(t){e.dialogFormVisible=t}}},[n("el-form",{ref:"UserInfo",attrs:{model:e.UserInfo}},[n("el-form-item",{attrs:{label:"用户名","label-width":e.formLabelWidth}},[n("el-input",{attrs:{disabled:!0},model:{value:e.UserInfo.username,callback:function(t){e.$set(e.UserInfo,"username",t)},expression:"UserInfo.username"}})],1),n("el-form-item",{attrs:{label:"姓名","label-width":e.formLabelWidth}},[n("el-input",{model:{value:e.UserInfo.name,callback:function(t){e.$set(e.UserInfo,"name",t)},expression:"UserInfo.name"}})],1),n("el-form-item",{attrs:{label:"人脸识别头像","label-width":e.formLabelWidth}},[n("div",{staticStyle:{width:"120px",height:"120px"},attrs:{id:"perEditHead"}}),n("el-upload",{ref:"profile",staticClass:"upload-demo",attrs:{prop:"profile",action:"","on-preview":e.handlePreview,"on-remove":e.handleRemove,"before-remove":e.beforeRemove,"on-change":e.getFile,multiple:"",limit:1,"on-exceed":e.handleExceed,"auto-upload":!1}},[n("el-button",{attrs:{size:"small",type:"primary"}},[e._v("更换头像")])],1)],1)],1),n("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[n("el-button",{on:{click:function(t){e.dialogFormVisible=!1}}},[e._v("取 消")]),n("el-button",{attrs:{type:"primary"},on:{click:function(t){e.editPerInfo()}}},[e._v("确 定")])],1)],1)],1)},o=[],i=(n("RW0V"),n("rGqo"),n("f3/d"),n("ssfR")),a=n("tvBP"),s=n("7Qib"),u={name:"MyHeader",created:function(){this.getPhoto()},data:function(){return{BASE_URL:"/",note:{backgroundImage:"url("+n("mWCa")+")",backgroundRepeat:"no-repeat",height:"60px",width:"100%",backgroundSize:"100% 100%",position:"relative"},UserInfo:{username:"",name:"",profile:null},userHeadPhoto:null,submitUserInfo:{name:""},dialogFormVisible:!1,formLabelWidth:"100px"}},computed:{editPerInfoFormData:function(){var e=this;this.submitUserInfo.name=this.UserInfo.name,null!=this.userHeadPhoto&&(this.submitUserInfo.profile=this.userHeadPhoto);var t=new FormData;return console.log(this.submitUserInfo),Object.keys(this.submitUserInfo).forEach(function(n){t.set(n,e.submitUserInfo[n])}),t}},methods:{getFile:function(e,t){this.userHeadPhoto=e.raw},handleRemove:function(e,t){console.log(e,t),this.fileList=[]},handlePreview:function(e){console.log(e)},handleExceed:function(e,t){this.$message.warning("当前限制选择 1 个文件")},beforeRemove:function(e,t){return this.$confirm("确定移除 ".concat(e.name,"？"))},logoutFunction:function(){var e=this;Object(i["c"])().then(function(){e.$message({message:"账户注销成功  正在跳转",type:"success"}),setTimeout(function(){window.location.href=e.BASE_URL},2e3)})},getPhoto:function(){var e=this;Object(a["a"])().then(function(t){document.getElementById("headphoto").style.backgroundImage="url("+t.profile+"?t="+Date.now()+")",document.getElementById("headphoto").style.backgroundSize="45px 45px",e.UserInfo=t})},editPerInfo:function(){var e=this;new Promise(function(t){var n=e.editPerInfoFormData,r=n.get("profile");if(r){var o=new Image;o.src=URL.createObjectURL(r),o.onload=function(){Object(s["b"])(o).then(function(e){n.set("profile",e),t(n)})}}else t(n)}).then(function(e){return Object(a["b"])(e)}).then(function(){e.dialogFormVisible=!1,e.$message("修改成功"),setTimeout(e.getPhoto(),1e3),e.$refs.profile.clearFiles(),e.userHeadPhoto=null})},showEditPerInfo:function(){this.dialogFormVisible=!0,Object(a["a"])().then(function(e){document.getElementById("perEditHead").style.backgroundImage="url("+e.profile+"?t="+Date.now()+")",document.getElementById("perEditHead").style.backgroundSize="120px 120px"})}}},c=u,l=(n("YN8A"),n("KHd+")),d=Object(l["a"])(c,r,o,!1,null,"f1511726",null);t["a"]=d.exports},mWCa:function(e,t,n){e.exports=n.p+"img/head3.d6783fb6.png"},qt8B:function(e,t,n){},ssfR:function(e,t,n){"use strict";n.d(t,"b",function(){return s}),n.d(t,"c",function(){return u}),n.d(t,"d",function(){return c}),n.d(t,"a",function(){return l});n("yt8O"),n("VRzm");var r=n("dRp0"),o=n("Qyje"),i=n.n(o),a="hasLoggedIn";function s(e,t){var n=r["b"].post("login",i.a.stringify({username:e,password:t})).then(r["a"]);return n.then(function(){return sessionStorage.setItem(a,"true")}),n}function u(){return r["b"].post("logout").then(r["a"]).then(function(e){return sessionStorage.removeItem(a)})}function c(e){return r["b"].post("register",e).then(r["a"])}function l(){return"true"===sessionStorage.getItem(a)}r["b"].get("hasLoggedIn").then(r["a"]).then(function(e){return sessionStorage.setItem(a,e?"true":"false")})},tvBP:function(e,t,n){"use strict";n.d(t,"a",function(){return o}),n.d(t,"b",function(){return i});var r=n("dRp0");function o(e){return r["b"].get("user",{params:{id:e}}).then(r["a"])}function i(e){return console.log(e.get("profile")),r["b"].post("user",e).then(r["a"])}},xhDR:function(e,t,n){"use strict";var r=n("zVlS"),o=n.n(r);o.a},zVlS:function(e,t,n){},za7x:function(e,t,n){"use strict";var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("img",{attrs:{src:e.src}})},o=[],i={name:"Icon",props:{src:{type:String,required:!0}}},a=i,s=(n("RPjt"),n("KHd+")),u=Object(s["a"])(a,r,o,!1,null,"72f3cb9a",null);t["a"]=u.exports},zbG2:function(e,t,n){"use strict";n.d(t,"d",function(){return a}),n.d(t,"a",function(){return s}),n.d(t,"c",function(){return u}),n.d(t,"b",function(){return c});n("yt8O"),n("VRzm");var r=n("dRp0"),o=n("Qyje"),i=n.n(o);function a(){return r["b"].get("check/status").then(r["a"])}function s(e,t){return t.append("id",e),r["b"].post("check/check",t).then(r["a"])}function u(e){return r["b"].post("check/enable",i.a.stringify({id:e})).then(r["a"])}function c(e){return r["b"].post("check/disable",i.a.stringify({id:e})).then(r["a"])}}}]);
//# sourceMappingURL=chunk-common.fc31d412.js.map