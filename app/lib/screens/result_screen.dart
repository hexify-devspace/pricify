import "package:flutter/material.dart";
import "package:flutter_screenutil/flutter_screenutil.dart";

class ResultScreen extends StatefulWidget {
  const ResultScreen({ Key? key }) : super(key: key);

  @override
  _ResultState createState() => _ResultState();
}

class _ResultState extends State<ResultScreen> {
  @override
  Widget build(BuildContext context) {
    ScreenUtil.init(context);

    return Scaffold(
        body: SafeArea(
            child: Stack(
                children: <Widget>[
                    Text("Result", style: TextStyle(color: Colors.white))
                ]
            )
        )
    );
  }
}
