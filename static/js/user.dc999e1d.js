(function(e){function t(t){for(var r,a,o=t[0],c=t[1],u=t[2],l=0,d=[];l<o.length;l++)a=o[l],s[a]&&d.push(s[a][0]),s[a]=0;for(r in c)Object.prototype.hasOwnProperty.call(c,r)&&(e[r]=c[r]);h&&h(t);while(d.length)d.shift()();return i.push.apply(i,u||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],r=!0,a=1;a<n.length;a++){var o=n[a];0!==s[o]&&(r=!1)}r&&(i.splice(t--,1),e=c(c.s=n[0]))}return e}var r={},a={3:0},s={3:0},i=[];function o(e){return c.p+"js/"+({5:"googleFaceDetectorComponent",6:"normalFaceDetectorComponent"}[e]||e)+"."+{5:"32a1b55d",6:"abedb653"}[e]+".js"}function c(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.e=function(e){var t=[],n={5:1,6:1};a[e]?t.push(a[e]):0!==a[e]&&n[e]&&t.push(a[e]=new Promise(function(t,n){for(var r="css/"+({5:"googleFaceDetectorComponent",6:"normalFaceDetectorComponent"}[e]||e)+"."+{5:"f1afcf69",6:"ffbba950"}[e]+".css",a=c.p+r,s=document.getElementsByTagName("link"),i=0;i<s.length;i++){var o=s[i],u=o.getAttribute("data-href")||o.getAttribute("href");if("stylesheet"===o.rel&&(u===r||u===a))return t()}var l=document.getElementsByTagName("style");for(i=0;i<l.length;i++){o=l[i],u=o.getAttribute("data-href");if(u===r||u===a)return t()}var d=document.createElement("link");d.rel="stylesheet",d.type="text/css",d.onload=t,d.onerror=function(t){var r=t&&t.target&&t.target.src||a,s=new Error("Loading CSS chunk "+e+" failed.\n("+r+")");s.request=r,n(s)},d.href=a;var h=document.getElementsByTagName("head")[0];h.appendChild(d)}).then(function(){a[e]=0}));var r=s[e];if(0!==r)if(r)t.push(r[2]);else{var i=new Promise(function(t,n){r=s[e]=[t,n]});t.push(r[2]=i);var u,l=document.getElementsByTagName("head")[0],d=document.createElement("script");d.charset="utf-8",d.timeout=120,c.nc&&d.setAttribute("nonce",c.nc),d.src=o(e),u=function(t){d.onerror=d.onload=null,clearTimeout(h);var n=s[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src,i=new Error("Loading chunk "+e+" failed.\n("+r+": "+a+")");i.type=r,i.request=a,n[1](i)}s[e]=void 0}};var h=setTimeout(function(){u({type:"timeout",target:d})},12e4);d.onerror=d.onload=u,l.appendChild(d)}return Promise.all(t)},c.m=e,c.c=r,c.d=function(e,t,n){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)c.d(n,r,function(t){return e[t]}.bind(null,r));return n},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="/",c.oe=function(e){throw console.error(e),e};var u=window["webpackJsonp"]=window["webpackJsonp"]||[],l=u.push.bind(u);u.push=t,u=u.slice();for(var d=0;d<u.length;d++)t(u[d]);var h=l;i.push([11,0,1]),n()})({"/4RH":function(e,t,n){},"/9jW":function(e,t,n){"use strict";var r=n("SPP6"),a=n.n(r);a.a},"/ZVV":function(e,t,n){},"/dQN":function(e,t,n){"use strict";var r=n("C7Uh"),a=n.n(r);a.a},"0/y/":function(e,t,n){},"0RpP":function(e,t){e.exports="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAHnUlEQVR4Xu2dS2hcZRTH/+cm4/QliMWCKC66CBQEpbqJDwrS1gcFt+qmxJreSc2980AUXbSJCCLSmeTOyMxNWiooKnRnNk11UQS1XbQbaX1hF4KC+KCgfaSTuUcybcbEjpoPv3sn33dPdiFnzjn////HZG5m8l2CfKXaAVqq/mBtasDh6FGANhrgSgscnecMTpRGRn7oxb5BMH1nC/PbQM5mAH292EFpJuMnh/njfD737eLjOgBMVhs5BgUAMkpNe1zMzPNE9EzBc48mucpkbeqpKIreIaL+JOdqmNUER88X/JHphV5tAIKgcU8LOENEjoYBvWjxVcFztyQ5uFINvyZgIMmZumYxc8RE95Y894s2ABNBOApCVdeAXvSJmhfXlUqly0nMDoIgG1H2ShKz4prBjH1F3623AahUwzECDsQ1LIm+Ds+t8X1/LolZ5XJ5rZNZfymJWXHNYGC86LkLuZsPAANni557d1xmdetbqYbnCEj0145OfdYAwIzfyMEThVH3lE6D/qtXpdYYJMaMIVdMN8hRAIBnGXTyvwzpwc/bl4F9yB73/Wd/7sF8vFmvb+pvYseqvQxkDBJhZzdvFABAqeC5lV4YLDP/nwOVWqNETAcFgP/no7GPFgCMjU7P4gKAHh+N7SIAGBudnsUFAD0+GttFADA2Oj2LCwB6fDS2iwBgbHR6FhcA9PhobBcBwNjo9CwuAOjx0dguAoCx0elZXADQ46OxXQQAY6PTs7gAoMdHY7sIAMZGp2dxAUCPj8Z2EQCMjU7P4gKAHh+N7SIAGBudnsUFAD0+GttFADA2Oj2LCwB6fDS2iwBgbHR6FhcA9PhobBcBwNjo9CwuAOjx0dguAoCx0elZXADQ46OxXQQAY6PTs7gAoMdHY7sIAMZGp2dxAUCPj8Z2EQCMjU7P4gKAHh+N7SIAGBudnsVXDMBE0NgPovFuYwlcyHu5ST0rSZckHagEYYEIXQ/4ImAs77nj1w6KDBpPE9F7XQGI+PF8PncsycVllh4HFg60Zub3u3fj5wpe7nAbgCNHjqy58MfVMzecfMk4vTaLQdd1m3pWki5JOlCphLdTP38D0Ialc5lxFf2tLcV9+853josvlw/d6mRaVTB2MDAPwszVdf0vvLRnz+9JLi2z9DpQDsKdDvAuCLe1OzMugGh3wdv74cK3y24YoXe0dDPBAQHAhJRi3FEAiNFcE1oLACakFOOOAkCM5prQWgAwIaUYdxQAYjTXhNYCgAkpxbijABCjuSa0FgBMSCnGHZcBUKnWHwRoq6k3QorRJ0ta869O5JzO5/d+tiioA0AlCD8iwnZLlIqMf3WAZwte7rHOewHlYPphh6JPxLX0OMCIHip6I58u3jrWB0E+9JGe/MGE0eKo+1YbgMlqI8+giRTpT71UBvtFL1e9BsDk1APs8KepdyVFBjjsDPr+8Mm/XgRWwzcIeDFFHqRWKoNfL3q5VzovAhedKFcb9ztMDzDh1tS6Y7XwhcvAvs/y+eHTN1wGWq1bxP2jA/KXwJTDIQAIACl3IOXy5RlAAEi5AymXL88AAkDKHUi5fHkGEABS7kDK5S95L2D6EXD0MoCtIJ4H6LQT0WtLPz2Scq+MlP/G4cM3Zy81DzLTLhD3gWkWrZv8YnHoQue9gIX/DKb+1vdEWL9UJTN+4fmLd5VKpctGqk/50mEYZi7P4XMQ7luWK/DlLRtu2jo0NHTl2tvBtXA3M97u7hc9ufivxCn30zj5E7WpXWCe6bY4ET2dH937wfUPhIQHGBjrWihHxBgX/OLCE9WwCKDcVQDzgYKfe/X6R8Ia4yDa/w9KSwXP7XrOjLHOpGRxlUOiBAALoRAALAxVRZIAoOKWhbUCgIWhqkgSAFTcsrBWALAwVBVJAoCKWxbWCgAWhqoiSQBQccvCWgHAwlBVJAkAKm5ZWCsAWBiqiiQBQMUtC2sFAAtDVZEkAKi4ZWGtAGBhqCqSBAAVtyysFQAsDFVFkgCg4paFtQKAhaGqSBIAVNyysFYAsDBUFUkCgIpbFtYKABaGqiJJAFBxy8JaAcDCUFUkCQAqbllYKwBYGKqKJAFAxS0LawUAC0NVkSQAqLhlYa0AYGGoKpIEABW3LKwVACwMVUWSAKDiloW1AoCFoapI0gQAzzLopMrghGpb4Og8Z3CiNDLyQ0Izl40Jguk7W5jfBnI2A+jrxQ7/OpMxSISd3WoYGC967thKTglbdbqWLsTM80T0TMFzjya56GRt6qkoit4hov4k5+qaZQ0A1w35quC5W3SZs5I+lWr4NQEDK6ldjTW2AYCoeXFdUkfaBkGQjSh7ZTUGu9Kd/gZA6ILQWOmDV2Odw3NrfN+fS2K3crm81smsv5TErLhmcIThYt491H4NUK7X73Ca9B2IsnENjLMvA2eLnnt3nDP+3rtSDc8RkOivHW36mOf6KLPZ8/b82DkufiKoD4OctwBktA1KoBEzfiMHTxRG3VMJjOuMqNQag8SYAWhjknM1zGoCPFLwcocXei27Y8jB2tRAH0fbGbRJw6C4W7QvA/uQPe77z/4c97Bu/d+s1zf1N7Fj1V4G3rD0wq1jcSyfz327+CO5ZUwvyFlFM/8EJ8pNzBpq5jYAAAAASUVORK5CYII="},11:function(e,t,n){e.exports=n("8Ebm")},"2kZ5":function(e,t,n){},"3Giy":function(e,t,n){},"6Ccb":function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-card",{staticClass:"schedule",style:"background-color: "+e.scheduleColor,attrs:{shadow:e.type===e.scheduleTypes.open?"hover":"never"}},[n("h4",[e._v(e._s(e.startUpTime))]),n("span",[e._v(e._s(e.groupName))])])},a=[],s=(n("rGqo"),n("RW0V"),n("dRSK"),{missed:"missed",done:"done",open:"open",future:"future"}),i={name:"Schedule",props:{type:{type:String,required:!0,validator:function(e){return Object.keys(s).find(function(t){return s[t]===e})}},groupId:{type:String,required:!0},groupName:{type:String,required:!0},startUpTime:{type:String,required:!0}},data:function(){return{scheduleTypes:s}},computed:{scheduleColor:function(){switch(this.type){case s.missed:return"rgba(136, 138, 143, 0.45)";case s.done:return"rgba(149, 235, 106, 0.5)";case s.open:return"rgba(230, 162, 60, 0.41)";case s.future:return"#71c2f145"}}}},o=i,c=(n("Qe7a"),n("ukju"),n("KHd+")),u=Object(c["a"])(o,r,a,!1,null,"8a02a050",null);t["default"]=u.exports},"6fLH":function(e,t,n){"use strict";var r=n("2kZ5"),a=n.n(r);a.a},"7rWN":function(e,t,n){},"8Ebm":function(e,t,n){"use strict";n.r(t);n("yt8O"),n("VRzm");var r=n("Kw5r"),a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{attrs:{id:"app"}},[n("router-view")],1)},s=[],i=(n("6fLH"),n("KHd+")),o={},c=Object(i["a"])(o,a,s,!1,null,null,null),u=c.exports,l=n("jE9Z"),d=n("7Qib"),h=n("ssfR"),f=n("vhw6"),p=function(e){return f("./".concat(Object(d["c"])(e),"/").concat(Object(d["d"])(e),".vue")).default};r["default"].use(l["a"]);var m=new l["a"]({routes:[{path:"/",name:"home",component:p("home")},{path:"/group/:id",name:"group",props:!0,component:p("group")}]});m.beforeEach(function(e,t,n){Object(h["a"])()?n():window.location.href="/#/login?redirect=".concat(encodeURIComponent(location.href))});var v=n("XJYT"),g=n.n(v),j=(n("D66Q"),n("iD6I"),n("SeeR")),b=n.n(j);r["default"].config.productionTip=!1,r["default"].use(g.a),new b.a,new r["default"]({router:m,render:function(e){return e(u)}}).$mount("#app")},BEVL:function(e,t,n){},C7Uh:function(e,t,n){},FnVl:function(e,t,n){"use strict";var r=n("W4NO"),a=n.n(r);a.a},GyN7:function(e,t,n){"use strict";var r=n("Ppca"),a=n.n(r);a.a},I85W:function(e,t,n){"use strict";var r=n("/4RH"),a=n.n(r);a.a},JScS:function(e,t,n){"use strict";var r=n("7rWN"),a=n.n(r);a.a},MoCw:function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"home"},[r("my-header"),r("el-form",[r("el-form-item",[r("el-input",{attrs:{type:"text",placeholder:"输入群组口令"},model:{value:e.searchId,callback:function(t){e.searchId=t},expression:"searchId"}},[r("el-button",{attrs:{slot:"append",icon:"el-icon-search"},on:{click:e.searchButtonHandler},slot:"append"}),r("el-button",{attrs:{slot:"append"},on:{click:e.handleIconScanClick},slot:"append"},[r("img",{staticClass:"icon_scan",attrs:{src:n("0RpP")}})])],1)],1)],1),r("section",{staticClass:"main"},[r("today-schedule-table"),r("group-joined-list")],1),e.isScanningQRCode?r("q-r-code-scanner",{on:{detected:e.handleDetectedQRCode}}):e._e()],1)},a=[],s=(n("SRfc"),function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"today-schedule-table"},[n("my-title",{staticClass:"title",staticStyle:{color:"white"}},[e._v("今日签到")]),n("el-collapse",{staticStyle:{overflow:"hidden"},model:{value:e.activeNames,callback:function(t){e.activeNames=t},expression:"activeNames"}},[n("el-collapse-item",{attrs:{title:"错过签到",name:"missed"}},[0!==e.missedList.length?n("ul",e._l(e.missedList,function(t){return n("li",{key:Math.random()},[n("schedule",e._b({attrs:{type:"missed"}},"schedule",t,!1))],1)})):n("div",{staticClass:"no-data"},[e._v("暂无数据")])]),n("el-collapse-item",{attrs:{title:"成功签到",name:"done"}},[0!==e.doneList.length?n("ul",e._l(e.doneList,function(t){return n("li",{key:Math.random()},[n("schedule",e._b({attrs:{type:"done"}},"schedule",t,!1))],1)})):n("div",{staticClass:"no-data"},[e._v("暂无数据")])]),n("el-collapse-item",{attrs:{title:"正在签到",name:"open"}},[0!==e.openList.length?n("ul",e._l(e.openList,function(t){return n("li",{key:Math.random()},[n("schedule",e._b({attrs:{type:"open"}},"schedule",t,!1))],1)})):n("div",{staticClass:"no-data"},[e._v("暂无数据")])]),n("el-collapse-item",{attrs:{title:"即将开启",name:"future"}},[0!==e.futureList.length?n("ul",e._l(e.futureList,function(t){return n("li",{key:Math.random()},[n("schedule",e._b({attrs:{type:"future"}},"schedule",t,!1))],1)})):n("div",{staticClass:"no-data"},[e._v("暂无数据")])])],1)],1)}),i=[],o=n("zbG2"),c=n("6Ccb"),u=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"my-title",staticStyle:{color:"white"}},[n("div",{staticClass:"inner-wrapper"},[e._t("default")],2)])},l=[],d={name:"MyTitle"},h=d,f=(n("fd7q"),n("KHd+")),p=Object(f["a"])(h,u,l,!1,null,"37e9f024",null),m=p.exports,v={name:"TodayScheduleList",components:{MyTitle:m,Schedule:c["default"]},created:function(){var e=this;Object(o["d"])().then(function(t){e.doneList=t.done,e.missedList=t.missed,e.openList=t.open,e.futureList=t.future})},data:function(){return{doneList:[],missedList:[],openList:[],futureList:[],activeNames:["open"]}}},g=v,j=(n("bkWq"),Object(f["a"])(g,s,i,!1,null,"71be893b",null)),b=j.exports,w=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"group-joined-list"},[n("my-title",[e._v("已加入的群组")]),n("ul",e._l(e.groupInfoList,function(e){return n("li",[n("group-item",{attrs:{id:e.id}})],1)}))],1)},C=[],y=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("router-link",{staticClass:"group-item",attrs:{to:"/group/"+e.id}},[e.loading?n("i",{staticClass:"el-icon-loading"}):e._e(),e._v(e._s(e.loading?"":e.name)+"\n    "),n("i",{staticClass:"group-item__arrow el-icon-arrow-right"})])},A=[],k=(n("f3/d"),n("J9k6")),x={name:"GroupItem",props:{id:{type:String,required:!0}},created:function(){this.update()},data:function(){return{name:"",loading:!0}},methods:{update:function(){var e=this;this.loading=!0,Object(k["c"])(this.id).then(function(t){e.loading=!1,e.name=t.name})}}},O=x,D=(n("x7tS"),Object(f["a"])(O,y,A,!1,null,"7c3e1d10",null)),S=D.exports,B={name:"GroupJoinedList",components:{MyTitle:m,GroupItem:S},created:function(){this.update()},data:function(){return{groupInfoList:[]}},methods:{update:function(){var e=this;Object(k["d"])().then(function(t){e.groupInfoList=t})}}},I=B,R=(n("ZJ5A"),Object(f["a"])(I,w,C,!1,null,"8e13e98a",null)),L=R.exports,_=n("mDl2"),M=n("za7x"),E=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"QR-code-scanner"},[n("video",{ref:"video"}),n("canvas",{ref:"canvas",class:[e.showCanvas?"":"hidden"]})])},z=[],F=(n("ls82"),n("MECJ")),N=n("7Ozu"),Q=n.n(N),T=null,V={name:"QRCodeScanner",data:function(){return{video:null,canvas:null,showCanvas:!1}},mounted:function(){var e=Object(F["a"])(regeneratorRuntime.mark(function e(){var t,n,r;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return t=this.video=this.$refs.video,n=this.canvas=this.$refs.canvas,e.next=3,navigator.mediaDevices.getUserMedia({video:{facingMode:"environment"}});case 3:return r=e.sent,t.srcObject=r,e.next=7,new Promise(function(e){t.onloadedmetadata=function(){e(),console.log(r),t.play(),n.width=t.videoWidth,n.height=t.videoHeight}});case 7:T=requestAnimationFrame(this.scanner);case 8:case"end":return e.stop()}},e,this)}));return function(){return e.apply(this,arguments)}}(),beforeDestroy:function(){cancelAnimationFrame(T)},methods:{highlightArea:function(){var e=null;return function(t,n,r,a){var s=this,i=this.canvas,o=this.canvas.getContext("2d");o.clearRect(0,0,i.width,i.height),o.strokeStyle="#FF3B58",o.lineWidth=10,o.strokeRect(t,n,r,a),this.showCanvas=!0,clearTimeout(e),setTimeout(function(){s.showCanvas=!1},500)}}(),scanner:function(){var e=this.video,t=this.canvas,n=t.getContext("2d");n.drawImage(e,0,0,t.width,t.height);var r=n.getImageData(0,0,t.width,t.height),a=Q()(r.data,r.width,r.height);if(a){var s=a.location.topLeftCorner,i=s.x,o=s.y,c=a.location.topRightCorner.x-a.location.topLeftCorner.x,u=a.location.bottomLeftCorner.y-a.location.topLeftCorner.y;this.highlightArea(i,o,c,u),this.$emit("detected",a.data)}T=requestAnimationFrame(this.scanner)}}},P=V,H=(n("GyN7"),Object(f["a"])(P,E,z,!1,null,"3d9aa254",null)),W=H.exports,J={name:"home",components:{QRCodeScanner:W,Icon:M["a"],MyHeader:_["a"],GroupJoinedList:L,TodayScheduleTable:b},created:function(){},data:function(){return{BASE_URL:"/",searchId:"",isScanningQRCode:!1}},methods:{searchButtonHandler:function(){!this.searchId||this.searchId&&0===this.searchId.length?this.$alert("群组ID不可为空"):this.$router.push("/group/".concat(this.searchId))},handleIconScanClick:function(){this.isScanningQRCode=!0},handleDetectedQRCode:function(e){this.isScanningQRCode&&(this.isScanningQRCode=!1,e.match(/\\group\\[a-zA-Z]+/i)?(this.$message.success("检测到：".concat(e,"即将跳转到新的页面")),setTimeout(function(){location.href=e},2e3)):this.$message.error("检测到的内容：".concat(e," 中不含群组信息")))}}},U=J,G=(n("/9jW"),n("I85W"),Object(f["a"])(U,r,a,!1,null,"19fcc4c4",null));t["default"]=G.exports},PAU9:function(e,t,n){},PBxG:function(e,t,n){},Ppca:function(e,t,n){},Qe7a:function(e,t,n){"use strict";var r=n("PAU9"),a=n.n(r);a.a},RnhZ:function(e,t,n){var r={"./af":"K/tc","./af.js":"K/tc","./ar":"jnO4","./ar-dz":"o1bE","./ar-dz.js":"o1bE","./ar-kw":"Qj4J","./ar-kw.js":"Qj4J","./ar-ly":"HP3h","./ar-ly.js":"HP3h","./ar-ma":"CoRJ","./ar-ma.js":"CoRJ","./ar-sa":"gjCT","./ar-sa.js":"gjCT","./ar-tn":"bYM6","./ar-tn.js":"bYM6","./ar.js":"jnO4","./az":"SFxW","./az.js":"SFxW","./be":"H8ED","./be.js":"H8ED","./bg":"hKrs","./bg.js":"hKrs","./bm":"p/rL","./bm.js":"p/rL","./bn":"kEOa","./bn.js":"kEOa","./bo":"0mo+","./bo.js":"0mo+","./br":"aIdf","./br.js":"aIdf","./bs":"JVSJ","./bs.js":"JVSJ","./ca":"1xZ4","./ca.js":"1xZ4","./cs":"PA2r","./cs.js":"PA2r","./cv":"A+xa","./cv.js":"A+xa","./cy":"l5ep","./cy.js":"l5ep","./da":"DxQv","./da.js":"DxQv","./de":"tGlX","./de-at":"s+uk","./de-at.js":"s+uk","./de-ch":"u3GI","./de-ch.js":"u3GI","./de.js":"tGlX","./dv":"WYrj","./dv.js":"WYrj","./el":"jUeY","./el.js":"jUeY","./en-au":"Dmvi","./en-au.js":"Dmvi","./en-ca":"OIYi","./en-ca.js":"OIYi","./en-gb":"Oaa7","./en-gb.js":"Oaa7","./en-ie":"4dOw","./en-ie.js":"4dOw","./en-il":"czMo","./en-il.js":"czMo","./en-nz":"b1Dy","./en-nz.js":"b1Dy","./eo":"Zduo","./eo.js":"Zduo","./es":"iYuL","./es-do":"CjzT","./es-do.js":"CjzT","./es-us":"Vclq","./es-us.js":"Vclq","./es.js":"iYuL","./et":"7BjC","./et.js":"7BjC","./eu":"D/JM","./eu.js":"D/JM","./fa":"jfSC","./fa.js":"jfSC","./fi":"gekB","./fi.js":"gekB","./fo":"ByF4","./fo.js":"ByF4","./fr":"nyYc","./fr-ca":"2fjn","./fr-ca.js":"2fjn","./fr-ch":"Dkky","./fr-ch.js":"Dkky","./fr.js":"nyYc","./fy":"cRix","./fy.js":"cRix","./gd":"9rRi","./gd.js":"9rRi","./gl":"iEDd","./gl.js":"iEDd","./gom-latn":"DKr+","./gom-latn.js":"DKr+","./gu":"4MV3","./gu.js":"4MV3","./he":"x6pH","./he.js":"x6pH","./hi":"3E1r","./hi.js":"3E1r","./hr":"S6ln","./hr.js":"S6ln","./hu":"WxRl","./hu.js":"WxRl","./hy-am":"1rYy","./hy-am.js":"1rYy","./id":"UDhR","./id.js":"UDhR","./is":"BVg3","./is.js":"BVg3","./it":"bpih","./it.js":"bpih","./ja":"B55N","./ja.js":"B55N","./jv":"tUCv","./jv.js":"tUCv","./ka":"IBtZ","./ka.js":"IBtZ","./kk":"bXm7","./kk.js":"bXm7","./km":"6B0Y","./km.js":"6B0Y","./kn":"PpIw","./kn.js":"PpIw","./ko":"Ivi+","./ko.js":"Ivi+","./ky":"lgnt","./ky.js":"lgnt","./lb":"RAwQ","./lb.js":"RAwQ","./lo":"sp3z","./lo.js":"sp3z","./lt":"JvlW","./lt.js":"JvlW","./lv":"uXwI","./lv.js":"uXwI","./me":"KTz0","./me.js":"KTz0","./mi":"aIsn","./mi.js":"aIsn","./mk":"aQkU","./mk.js":"aQkU","./ml":"AvvY","./ml.js":"AvvY","./mn":"lYtQ","./mn.js":"lYtQ","./mr":"Ob0Z","./mr.js":"Ob0Z","./ms":"6+QB","./ms-my":"ZAMP","./ms-my.js":"ZAMP","./ms.js":"6+QB","./mt":"G0Uy","./mt.js":"G0Uy","./my":"honF","./my.js":"honF","./nb":"bOMt","./nb.js":"bOMt","./ne":"OjkT","./ne.js":"OjkT","./nl":"+s0g","./nl-be":"2ykv","./nl-be.js":"2ykv","./nl.js":"+s0g","./nn":"uEye","./nn.js":"uEye","./pa-in":"8/+R","./pa-in.js":"8/+R","./pl":"jVdC","./pl.js":"jVdC","./pt":"8mBD","./pt-br":"0tRk","./pt-br.js":"0tRk","./pt.js":"8mBD","./ro":"lyxo","./ro.js":"lyxo","./ru":"lXzo","./ru.js":"lXzo","./sd":"Z4QM","./sd.js":"Z4QM","./se":"//9w","./se.js":"//9w","./si":"7aV9","./si.js":"7aV9","./sk":"e+ae","./sk.js":"e+ae","./sl":"gVVK","./sl.js":"gVVK","./sq":"yPMs","./sq.js":"yPMs","./sr":"zx6S","./sr-cyrl":"E+lV","./sr-cyrl.js":"E+lV","./sr.js":"zx6S","./ss":"Ur1D","./ss.js":"Ur1D","./sv":"X709","./sv.js":"X709","./sw":"dNwA","./sw.js":"dNwA","./ta":"PeUW","./ta.js":"PeUW","./te":"XLvN","./te.js":"XLvN","./tet":"V2x9","./tet.js":"V2x9","./tg":"Oxv6","./tg.js":"Oxv6","./th":"EOgW","./th.js":"EOgW","./tl-ph":"Dzi0","./tl-ph.js":"Dzi0","./tlh":"z3Vd","./tlh.js":"z3Vd","./tr":"DoHr","./tr.js":"DoHr","./tzl":"z1FC","./tzl.js":"z1FC","./tzm":"wQk9","./tzm-latn":"tT3J","./tzm-latn.js":"tT3J","./tzm.js":"wQk9","./ug-cn":"YRex","./ug-cn.js":"YRex","./uk":"raLr","./uk.js":"raLr","./ur":"UpQW","./ur.js":"UpQW","./uz":"Loxo","./uz-latn":"AQ68","./uz-latn.js":"AQ68","./uz.js":"Loxo","./vi":"KSF8","./vi.js":"KSF8","./x-pseudo":"/X5v","./x-pseudo.js":"/X5v","./yo":"fzPg","./yo.js":"fzPg","./zh-cn":"XDpg","./zh-cn.js":"XDpg","./zh-hk":"SatO","./zh-hk.js":"SatO","./zh-tw":"kOpN","./zh-tw.js":"kOpN"};function a(e){var t=s(e);return n(t)}function s(e){var t=r[e];if(!(t+1)){var n=new Error("Cannot find module '"+e+"'");throw n.code="MODULE_NOT_FOUND",n}return t}a.keys=function(){return Object.keys(r)},a.resolve=s,e.exports=a,a.id="RnhZ"},SPP6:function(e,t,n){},SeeR:function(e,t,n){e.exports=function(){return new Worker(n.p+"e2a6833f2d09d0efa10f.worker.js")}},TUJs:function(e,t,n){"use strict";var r=n("jNmN"),a=n.n(r);a.a},W4NO:function(e,t,n){},X3XN:function(e,t,n){},YJn7:function(e,t,n){},ZJ5A:function(e,t,n){"use strict";var r=n("0/y/"),a=n.n(r);a.a},biOa:function(e,t,n){"use strict";var r=n("c5Iq"),a=n.n(r);a.a},bkWq:function(e,t,n){"use strict";var r=n("BEVL"),a=n.n(r);a.a},c5Iq:function(e,t,n){},cfcG:function(e,t,n){"use strict";n.d(t,"a",function(){return o});n("ls82");var r=n("MECJ"),a=n("xmWZ"),s=n("qpph"),i=n("7Qib"),o=function(){function e(t){Object(a["a"])(this,e),this.video=t,this.faceDetector=new window.FaceDetector}return Object(s["a"])(e,[{key:"detect",value:function(){var e=Object(r["a"])(regeneratorRuntime.mark(function e(){var t,n,a,s,o,c;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return t={width:320,height:140},e.next=3,Object(i["a"])(this.video,{boxConstraint:t});case 3:return n=this.currentDetectingImageFile=e.sent,a=Math.min(t.width/this.video.videoWidth,t.height/this.video.videoHeight),s={width:this.video.videoWidth*a,height:this.video.videoHeight*a},e.next=8,new Promise(function(){var e=Object(r["a"])(regeneratorRuntime.mark(function e(t){var r;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:r=new Image,r.src=URL.createObjectURL(n),r.onload=function(){t(r)};case 3:case"end":return e.stop()}},e,this)}));return function(t){return e.apply(this,arguments)}}());case 8:return o=e.sent,e.prev=9,this.currentDetectingImageFile=n,e.next=13,this.faceDetector.detect(o);case 13:return c=e.sent,e.abrupt("return",c.map(function(e){return{x:e.boundingBox.left/s.width,y:e.boundingBox.top/s.height,width:e.boundingBox.width/s.width,height:e.boundingBox.height/s.height}}));case 17:e.prev=17,e.t0=e["catch"](9),console.error(e.t0);case 20:case"end":return e.stop()}},e,this,[[9,17]])}));return function(){return e.apply(this,arguments)}}()}],[{key:"support",value:function(){return!1}}]),e}()},fDTC:function(e,t,n){"use strict";n.r(t);var r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"group"},[n("app-bar",{style:e.note},[[n("span",{staticStyle:{color:"white","font-size":"1.3em","letter-spacing":"7.5px"}},[e._v(e._s(e.name))])],n("template",{slot:"right"},[n("el-button",{staticStyle:{"margin-right":"1em",color:"white"},attrs:{type:"text"},on:{click:e.quitGroup}},[e._v("退出群组")])],1)],2),n("section",{staticClass:"content"},[e.ownerName?n("div",{staticClass:"owner-tag"},[n("div",{staticClass:"owner-tag__key",staticStyle:{color:"white"}},[e._v("创建者：")]),n("div",{staticClass:"owner-tag__value"},[e._v(e._s(e.ownerName))])]):e._e(),e.loading?e._e():n("div",{staticClass:"group-operation"},[e.state?e.checked?n("el-button",{attrs:{type:"success",disabled:""}},[e._v("\n                "+e._s(e.checked?"已完成签到":"签到")+"\n            ")]):n("div",{staticClass:"check-button-wrapper"},[n("check-button",{on:{click:e.check}})],1):n("el-alert",{attrs:{title:"暂未开启签到",type:"warning"}}),e.hasJoined?e._e():n("have-not-joined",{attrs:{id:e.id},on:{hasJoined:e.hasJoinedHandler}})],1),!e.loading&&e.hasJoined?n("checking-history",{attrs:{id:e.id}}):n("i",{staticClass:"el-icon-loading"})],1),n("check-validator",{ref:"checkValidator",attrs:{"group-id":e.id}})],1)},a=[],s=(n("ls82"),n("MECJ")),i=(n("f3/d"),n("yt8O"),n("VRzm"),n("J9k6")),o=n("3TiO"),c=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"have-not-joined__wrapper"},[n("el-button",{staticClass:"join-button",attrs:{disabled:e.loading,type:"success"},on:{click:e.joinGroup}},[e.loading?n("i",{staticClass:"el-icon-loading"}):e._e(),e._v(e._s(e.loading?"":"加入")+"\n    ")])],1)},u=[],l={name:"HaveNotJoined",props:{id:{required:!0,type:String}},data:function(){return{loading:!1}},methods:{joinGroup:function(){var e=this,t=function(){e.loading=!1};this.loading=!0,Object(i["e"])(this.id).then(function(){e.$emit("hasJoined")},function(t){e.$message.error("发生错误：".concat(t.message))}).then(t,t)}}},d=l,h=(n("up1R"),n("KHd+")),f=Object(h["a"])(d,c,u,!1,null,"20c95409",null),p=f.exports,m=n("tvBP"),v=n("za7x"),g=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-button",{staticClass:"icon-more button-more",attrs:{type:"text",icon:"el-icon-more"}})},j=[],b={name:"ButtonMore"},w=b,C=(n("r00G"),Object(h["a"])(w,g,j,!1,null,"7030c420",null)),y=C.exports,A=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"check-validator"},[n("el-dialog",{attrs:{visible:e.visible,width:"100%"},on:{"update:visible":function(t){e.visible=t}}},[n("i",{staticClass:"el-icon-loading"}),e._v(e._s(e.message)+"\n    ")]),n("real-face-capture",{directives:[{name:"show",rawName:"v-show",value:e.faceCaptureVisible,expression:"faceCaptureVisible"}],ref:"faceCapture"})],1)},k=[],x=n("zbG2"),O=n("7Qib"),D=n("cfcG"),S={name:"CheckValidator",components:{RealFaceCapture:function(){return D["a"].support()?n.e(5).then(n.bind(null,"6z2l")):n.e(6).then(n.bind(null,"R1jR"))}},props:{groupId:{type:String,required:!0}},created:function(){},data:function(){return{visible:!1,faceCaptureVisible:!1,message:""}},methods:{check:function(){var e=Object(s["a"])(regeneratorRuntime.mark(function e(){var t,n,r,a,s,i=this,o=arguments;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:if(t=o.length>0&&void 0!==o[0]&&o[0],n=o.length>1&&void 0!==o[1]&&o[1],this.visible=!0,e.prev=3,this.message="正在签到",r=null,a=null,!t){e.next=21;break}return e.prev=8,this.message="正在获取地理位置",e.next=12,Object(O["b"])();case 12:r=e.sent,this.message="成功获取位置信息",Object(O["e"])(1e3),e.next=21;break;case 17:throw e.prev=17,e.t0=e["catch"](8),"NOT_SUPPORTED"===e.t0.info?this.$message.error("获取地理位置失败：当前浏览器不支持定位功能"):this.$message.error("获取地理位置失败："+e.t0.message),e.t0;case 21:if(!n){e.next=36;break}return this.message="正在获取人脸信息",this.faceCaptureVisible=!0,this.visible=!1,e.next=27,new Promise(function(e){return i.$nextTick(function(){return e()})});case 27:return e.next=29,this.$refs.faceCapture.getNormalFrame();case 29:return a=e.sent,this.visible=!0,this.message="成功获取人脸信息",this.faceCaptureVisible=!1,e.next=35,Object(O["e"])(1e3);case 35:this.visible=!0;case 36:return this.message="正在连接服务器",s=new FormData,r&&(s.append("lng",r.lng),s.append("lat",r.lat)),a&&s.append("face",a),e.next=42,Object(x["a"])(this.groupId,s);case 42:return e.abrupt("return",!0);case 45:throw e.prev=45,e.t1=e["catch"](3),console.log(e.t1),this.$message.error(e.t1.message),e.t1;case 50:return e.prev=50,this.visible=!1,this.faceCaptureVisible=!1,e.finish(50);case 54:case"end":return e.stop()}},e,this,[[3,45,50,54],[8,17]])}));return function(){return e.apply(this,arguments)}}()}},B=S,I=(n("FnVl"),n("TUJs"),Object(h["a"])(B,A,k,!1,null,"38250555",null)),R=I.exports,L=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticClass:"check-button",on:{click:function(t){e.$emit("click")}}},[e._v("签到\n    "),n("div",{staticClass:"flow flow-1"}),n("div",{staticClass:"flow flow-2"}),n("div",{staticClass:"flow flow-3"})])},_=[],M={name:"CheckButton"},E=M,z=(n("biOa"),Object(h["a"])(E,L,_,!1,null,"76755dda",null)),F=z.exports,N=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("el-table",{directives:[{name:"loading",rawName:"v-loading",value:e.loading,expression:"loading"}],staticClass:"checking-history-table",staticStyle:{width:"100%"},attrs:{data:e.historyData,"row-class-name":e.tableRowClassName}},[n("el-table-column",{attrs:{align:"center",label:"时间"},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(e._s(e._f("dateFormat")(t.row.startUpDateTime)))]}}])}),n("el-table-column",{attrs:{align:"center",label:"状态"},scopedSlots:e._u([{key:"default",fn:function(t){return[e._v(e._s(t.row.checked?"成功":"失败"))]}}])})],1)},Q=[],T=n("VOVZ"),V=n("wd/R"),P=n.n(V),H={name:"CheckingHistory",created:function(){var e=Object(s["a"])(regeneratorRuntime.mark(function e(){return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return console.log(P()("2018-07-07T05:13:03Z").locale("zh-cn").format("M/D, HH:mm, dddd")),this.loading=!0,e.prev=2,e.next=5,Object(T["a"])(this.id);case 5:this.historyData=e.sent;case 6:return e.prev=6,this.loading=!1,e.finish(6);case 9:case"end":return e.stop()}},e,this,[[2,,6,9]])}));return function(){return e.apply(this,arguments)}}(),props:{id:{type:String,required:!0}},data:function(){return{historyData:[],loading:!0}},methods:{tableRowClassName:function(e){var t=e.row;e.rowIndex;return t.checked?"record-done":"record-missed"}},filters:{dateFormat:function(e){return P()(e).locale("zh-cn").format("M/D, HH:mm, dddd")}}},W=H,J=(n("/dQN"),Object(h["a"])(W,N,Q,!1,null,null,null)),U=J.exports,G={name:"Group",components:{CheckingHistory:U,CheckButton:F,CheckValidator:R,ButtonMore:y,Icon:v["a"],HaveNotJoined:p,AppBar:o["a"]},props:{id:{required:!0,type:String}},created:function(){this.update()},data:function(){return{ownerId:void 0,ownerName:void 0,name:"",hasJoined:!1,state:!1,checked:!1,loading:!1,needFace:!1,needLocation:!1,note:{backgroundImage:"url("+n("mWCa")+")",backgroundRepeat:"no-repeat",height:"60px",width:"100%",backgroundSize:"100% 100%",position:"relative"}}},watch:{id:function(){this.update()},ownerId:function(){var e=this;Object(m["a"])(this.ownerId).then(function(t){e.ownerName=t.name})}},methods:{check:function(){var e=this;this.$refs.checkValidator.check(this.needLocation,this.needFace).then(function(){e.update()})},update:function(){var e=this,t=function(){e.loading=!1};this.loading=!0,Object(i["c"])(this.id).then(function(t){e.name=t.name,e.ownerId=t.owner,e.hasJoined=1===t.role,e.state=t.state,e.checked=t.checked,e.needLocation=t.needLocation,e.needFace=t.needFace},function(e){return null}).then(t,t)},hasJoinedHandler:function(){this.update()},quitGroup:function(){var e=Object(s["a"])(regeneratorRuntime.mark(function e(){return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,this.$confirm("即将退出该群组, 是否继续?","提示",{confirmButtonText:"确定",cancelButtonText:"取消",type:"warning"});case 3:return e.next=5,Object(i["f"])(this.id);case 5:this.$message("退出成功"),this.$router.push({name:"home"}),e.next=12;break;case 9:e.prev=9,e.t0=e["catch"](0),this.$message.error(e.t0.message);case 12:case"end":return e.stop()}},e,this,[[0,9]])}));return function(){return e.apply(this,arguments)}}(),test:function(){alert(1)}}},K=G,Y=(n("JScS"),Object(h["a"])(K,r,a,!1,null,"48de83c8",null));t["default"]=Y.exports},fd7q:function(e,t,n){"use strict";var r=n("/ZVV"),a=n.n(r);a.a},iD6I:function(e,t,n){},jNmN:function(e,t,n){},r00G:function(e,t,n){"use strict";var r=n("X3XN"),a=n.n(r);a.a},ukju:function(e,t,n){"use strict";var r=n("3Giy"),a=n.n(r);a.a},up1R:function(e,t,n){"use strict";var r=n("PBxG"),a=n.n(r);a.a},vhw6:function(e,t,n){var r={"./group/Group":"fDTC","./group/Group.vue":"fDTC","./home/Home":"MoCw","./home/Home.vue":"MoCw","./home/components/Schedule":"6Ccb","./home/components/Schedule.vue":"6Ccb"};function a(e){var t=s(e);return n(t)}function s(e){var t=r[e];if(!(t+1)){var n=new Error("Cannot find module '"+e+"'");throw n.code="MODULE_NOT_FOUND",n}return t}a.keys=function(){return Object.keys(r)},a.resolve=s,e.exports=a,a.id="vhw6"},x7tS:function(e,t,n){"use strict";var r=n("YJn7"),a=n.n(r);a.a}});
//# sourceMappingURL=user.dc999e1d.js.map