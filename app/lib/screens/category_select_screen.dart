import "package:flutter/material.dart";
import "package:flutter_screenutil/flutter_screenutil.dart";

class CategorySelectScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    ScreenUtil.init(context, designSize: Size(375, 812));

    return Scaffold(
        body: SafeArea(
            child: Stack(children: <Widget>[
      Container(height: 44.h, width: 375.w, color: Color(0xFF000000)),
      Container(
          margin: EdgeInsets.only(top: 38.h, left: 52.w),
          width: 58.w,
          child: Text("STEP 1:",
              textAlign: TextAlign.left,
              style: TextStyle(
                  fontFamily: "Mulish",
                  fontSize: 16.sp,
                  color: Color(0xFFDCDCE4)))),
      Container(
          margin: EdgeInsets.only(top: 83.h, left: 24.w),
          width: 327.w,
          child: Text("Select the category you want to analyze:",
              textAlign: TextAlign.left,
              style: TextStyle(
                  fontFamily: "DM Sans",
                  fontSize: 22.sp,
                  color: Color(0xFFFFFFFF)))),
      Container(
          margin: EdgeInsets.only(top: 105.h, left: 24.w),
          width: 327.w,
          child: Text(
              "Please enter your new password twice so we can verify you typed it in correctly",
              textAlign: TextAlign.center,
              style: TextStyle(
                  fontFamily: "Mulish",
                  fontSize: 16.sp,
                  color: Color(0xFF8E8EA9)))),
      Container(
          margin: EdgeInsets.only(top: 167.h, left: 24.w),
          height: 212.h,
          width: 327.w,
          decoration: BoxDecoration(
              color: Color(0xFF4A4A6A),
              borderRadius: BorderRadius.all(Radius.circular(16.w)),
              boxShadow: [
                BoxShadow(
                    color: Color(0x0A323247),
                    blurRadius: 20.w,
                    offset: Offset(0.w, 4.h)),
                BoxShadow(color: Color(0x080C1A4B), blurRadius: 1.w)
              ])),
      Container(
          margin: EdgeInsets.only(top: 277.h, left: 44.w),
          child: Func_Electronic_Devices("Used Cars"),
          width: 227.w),
      Container(
          margin: EdgeInsets.only(top: 311.h, left: 44.w),
          height: 31.h,
          width: 31.w,
          decoration: BoxDecoration(
              color: Color(0xFFFFF2EA),
              borderRadius: BorderRadius.all(Radius.circular(8.w)))),
      Container(
          margin: EdgeInsets.only(top: 311.h, left: 44.w),
          child: Func_Get_your_electronics_right(
              "Know the best value you can get for your car all across the country"),
          width: 227.w),
      Container(
          margin: EdgeInsets.only(top: 315.h, left: 287.w),
          height: 44.h,
          width: 44.w,
          decoration: BoxDecoration(
              color: Color(0xFF892CFF),
              borderRadius: BorderRadius.all(Radius.circular(16.w)))),
      Container(
          margin: EdgeInsets.only(top: 403.h, left: 24.w),
          height: 188.h,
          width: 327.w,
          decoration: BoxDecoration(
              color: Color(0xFF4A4A6A),
              borderRadius: BorderRadius.all(Radius.circular(16.w)),
              boxShadow: [
                BoxShadow(
                    color: Color(0x0A323247),
                    blurRadius: 20.w,
                    offset: Offset(0.w, 4.h)),
                BoxShadow(color: Color(0x080C1A4B), blurRadius: 1.w)
              ])),
      Container(
          margin: EdgeInsets.only(top: 513.h, left: 44.w),
          child: Func_Electronic_Devices("Electronic Devices"),
          width: 227.w),
      Container(
          margin: EdgeInsets.only(top: 527.h, left: 287.w),
          height: 44.h,
          width: 44.w,
          decoration: BoxDecoration(
              color: Color(0xFFE12CFF),
              borderRadius: BorderRadius.all(Radius.circular(16.w)))),
      Container(
          margin: EdgeInsets.only(top: 547.h, left: 44.w),
          height: 31.h,
          width: 31.w,
          decoration: BoxDecoration(
              color: Color(0xFFFFF2EA),
              borderRadius: BorderRadius.all(Radius.circular(8.w)))),
      Container(
          margin: EdgeInsets.only(top: 547.h, left: 44.w),
          child: Func_Get_your_electronics_right("Get your electronics right"),
          width: 227.w),
      Container(
          margin: EdgeInsets.only(top: 766.h, left: 121.w),
          height: 5.h,
          width: 134.w,
          decoration: BoxDecoration(
              color: Color(0xFFFFFFFF),
              borderRadius: BorderRadius.all(Radius.circular(100.w))))
    ])));
  }

  Widget Func_Electronic_Devices(String characters) {
    return Text(characters,
        textAlign: TextAlign.left,
        style: TextStyle(
            fontFamily: "Mulish", fontSize: 16.sp, color: Color(0xFFFFFFFF)));
  }

  Widget Func_Get_your_electronics_right(String characters) {
    return Text(characters,
        textAlign: TextAlign.left,
        style: TextStyle(
            fontFamily: "Mulish", fontSize: 14.sp, color: Color(0xFFC0C0CF)));
  }
}              
