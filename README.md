# DarkCluster Flutter

Aplicación de ejemplo construida con Flutter. Incluye un contador básico y prueba de widgets para validar la interacción del botón flotante.

## Requisitos
- Flutter 3.x instalado en tu entorno
- SDK de Dart 3.2 o superior

## Ejecutar la aplicación
Si el proyecto no incluye los directorios de plataforma (`android/`, `ios/`, `web/`, etc.), genera el andamiaje antes de intentar ejecutar la app:

```bash
flutter create --platforms=android,ios,web,linux,macos,windows .
```

Luego:
```bash
flutter pub get
flutter run
```

## Ejecutar pruebas
```bash
flutter test
```
