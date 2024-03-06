#!/bin/bash

# Instalar las dependencias
pip install -r requirements.txt

# Establecer la variable de entorno para la API key de OpenAI
export OPENAI_API_KEY='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'

# Ejecutar la aplicación Flask
python main.py
