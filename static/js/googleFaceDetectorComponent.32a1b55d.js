(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[5],{"186L":function(e,t,r){"use strict";var n=r("e55S"),a=r.n(n);a.a},"6z2l":function(e,t,r){"use strict";r.r(t);var n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"face-capture container"},[r("video",{ref:"videoDisplayer",attrs:{width:"320",height:"140"}}),r("canvas",{ref:"canvasDisplayer",attrs:{width:"320",height:"240"}})])},a=[],i=(r("ls82"),r("MECJ")),o=(r("rGqo"),r("cfcG")),c=null,s={name:"FaceCapture2",created:function(){if(!o["a"].support())throw new Error("当前浏览器不支持google face detector api")},data:function(){return{faceDetector:null,detectorTimeoutId:null,lastDetectingTime:0,videoArea:{width:320,height:240}}},mounted:function(){var e=this;c=new Promise(function(t){e.faceDetector=new o["a"](e.$refs.videoDisplayer),t()})},beforeDestroy:function(){this.$refs.videoDisplayer.srcObject.getTracks().forEach(function(e){return e.stop()}),this.$refs.videoDisplayer.srcObject=null},methods:{getNormalFrame:function(){var e=Object(i["a"])(regeneratorRuntime.mark(function e(){var t,r,n,a,o=this;return regeneratorRuntime.wrap(function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,c;case 2:return e.next=4,navigator.mediaDevices.getUserMedia({video:!0});case 4:return t=e.sent,r=this.$refs.videoDisplayer,n=this.$refs.canvasDisplayer,a=n.getContext("2d"),r.srcObject=t,e.next=9,new Promise(function(e){r.onloadedmetadata=function(){return e()}});case 9:return r.play(),e.abrupt("return",new Promise(function(e){var t=function(){var r=Object(i["a"])(regeneratorRuntime.mark(function r(){var i,c,s,u;return regeneratorRuntime.wrap(function(r){while(1)switch(r.prev=r.next){case 0:return r.prev=0,r.next=3,o.faceDetector.detect();case 3:for(c in i=r.sent,a.clearRect(0,0,n.width,n.height),a.lineWidth=2,a.strokeStyle="red",i)s=c,a.strokeRect(Math.floor(s.x*o.videoArea.width),Math.floor(s.y*o.videoArea.height),Math.floor(s.width*o.videoArea.width),Math.floor(s.height*o.videoArea.height)),a.stroke();i.length>0?e(o.faceDetector.currentDetectingImageFile):(u=o.lastDetectingTime=Date.now(),o.detectorTimeoutId=setTimeout(t,Math.max(0,300-u+o.lastDetectingTime))),r.next=14;break;case 11:throw r.prev=11,r.t0=r["catch"](0),r.t0;case 14:case"end":return r.stop()}},r,this,[[0,11]])}));return function(){return r.apply(this,arguments)}}();t()}));case 11:case"end":return e.stop()}},e,this)}));return function(){return e.apply(this,arguments)}}()}},u=s,h=(r("186L"),r("KHd+")),f=Object(h["a"])(u,n,a,!1,null,"3ef7ce1f",null);t["default"]=f.exports},e55S:function(e,t,r){}}]);
//# sourceMappingURL=googleFaceDetectorComponent.32a1b55d.js.map