import 'package:darkcluster/main.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('Incrementa el contador cuando se presiona el botón', (tester) async {
    await tester.pumpWidget(const DarkClusterApp());

    expect(find.text('0'), findsOneWidget);
    expect(find.text('1'), findsNothing);

    await tester.tap(find.byIcon(Icons.add));
    await tester.pump();

    expect(find.text('1'), findsOneWidget);
  });

  testWidgets('Reinicia el contador al presionar el botón de reinicio', (tester) async {
    await tester.pumpWidget(const DarkClusterApp());

    await tester.tap(find.byIcon(Icons.add));
    await tester.pump();

    expect(find.text('1'), findsOneWidget);

    await tester.tap(find.widgetWithText(ElevatedButton, 'Reiniciar contador'));
    await tester.pump();

    expect(find.text('0'), findsOneWidget);
  });
}
