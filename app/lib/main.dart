import 'package:flutter/material.dart';
import 'screens/category_select_screen.dart';
import 'screens/filter_select_screen.dart';
import 'screens/result_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: 'Pricify',
        theme: new ThemeData(scaffoldBackgroundColor: const Color(0x4A4A6AFF)),
        initialRoute: '/step3',
        routes: {
          '/step1': (ctx) => CategorySelectScreen(),
          '/step2': (ctx) => FilterSelectScreen(),
          '/step3': (ctx) => ResultScreen(),
        });
  }
}
