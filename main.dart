import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  static const String _title = '@irdrop';

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: _title,
      home: Scaffold(
        appBar: AppBar(title: const Text(_title)),
        body: const MyStatefulWidget(),
      ),
    );
  }
}

class MyStatefulWidget extends StatefulWidget {
  const MyStatefulWidget({Key? key}) : super(key: key);

  @override
  State<MyStatefulWidget> createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {

  @override
  Widget build(BuildContext context) {
    return Padding(
        padding: const EdgeInsets.all(10),
        child: ListView(
          children: <Widget>[
            Container(
                alignment: Alignment.center,
                padding: const EdgeInsets.all(10),
                child: const Text(
                  'Link Share',
                  style: TextStyle(
                      color: Colors.blue,
                      fontWeight: FontWeight.w500,
                      fontSize: 30),
                )),
            Container(
              padding: const EdgeInsets.fromLTRB(10, 20, 10, 20),
              child: const TextField(
                decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Link',
                    hintText: 'Enter link'
                ),
              ),
            ),
            Container(
                height: 50,
                padding: const EdgeInsets.fromLTRB(120, 0, 120, 0),
                child: ElevatedButton(
                  child: const Text('Share to'),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => const Devices()),
                    );
                  },
                )
            ),
          ],
        ));
  }
}

class Devices extends StatelessWidget {
  const Devices({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
        padding: const EdgeInsets.all(10),
    child: ListView(
    children: <Widget>[
    Container(
        height: 80,
        padding: const EdgeInsets.fromLTRB(80, 10, 80, 10),
        child: ElevatedButton(
          child: const Text('Desktop'),
          onPressed: () {
            // Navigator.push(
            //   context,
            //   MaterialPageRoute(builder: (context) => const Devices()),
            // );
          },
        )
    ),
    Container(
        height: 80,
        padding: const EdgeInsets.fromLTRB(80, 10, 80, 10),
        child: ElevatedButton(
          child: const Text('Ipad'),
          onPressed: () {
            // Navigator.push(
            //   context,
            //   MaterialPageRoute(builder: (context) => const Devices()),
            //   );
            },
          )
        ),
      Container(
          height: 80,
          padding: const EdgeInsets.fromLTRB(80, 10, 80, 10),
          child: ElevatedButton(
            child: const Text('Back'),
            onPressed: () {
              Navigator.pop(
                context,
              );
            },
          )
      )
      ],
    ));
  }
}