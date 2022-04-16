import "package:flutter/material.dart";
import "package:flutter_screenutil/flutter_screenutil.dart";

class FilterSelectScreen extends StatefulWidget {
  const FilterSelectScreen({ Key? key }) : super(key: key);

  @override
  _FilterSelectState createState() => _FilterSelectState();
}

class _FilterSelectState extends State<FilterSelectScreen> {
  @override
  Widget build(BuildContext context) {
    ScreenUtil.init(context);

    return Scaffold(
        body: SafeArea(
            child: Stack(
                children: <Widget>[
                    Text("Filter", style: TextStyle(color: Colors.white))
                ]
            )
        )
    );
  }
}
