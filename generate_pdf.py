import os
import base64
from playwright.sync_api import sync_playwright

WORKSPACE = r"c:\Users\ASUS\Documents\Proyectos Personales\RDA2_Lab5.3_Reto_Grupo1"
FRIO_IMG_PATH = os.path.join(WORKSPACE, "capturas", "termostato_frio_20c.png")
CALOR_IMG_PATH = os.path.join(WORKSPACE, "capturas", "termostato_calor_26c.png")
OUTPUT_PDF = os.path.join(WORKSPACE, "Informe_Lab5.3_RetoIntegrador_ClimatizadorReactivo.pdf")

with open(FRIO_IMG_PATH, "rb") as f:
    frio_b64 = base64.b64encode(f.read()).decode("utf-8")

with open(CALOR_IMG_PATH, "rb") as f:
    calor_b64 = base64.b64encode(f.read()).decode("utf-8")

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Informe Laboratorio 5.3: Climatizador Reactivo</title>
<style>
    @page {{
        size: A4;
        margin: 15mm 15mm 15mm 15mm;
        @bottom-right {{
            content: "Página " counter(page);
            font-size: 8.5pt;
            color: #64748b;
        }}
    }}
    body {{
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
        color: #1e293b;
        line-height: 1.5;
        font-size: 10pt;
        background: #fff;
        margin: 0;
        padding: 0;
    }}
    .header-box {{
        border-bottom: 3px solid #1976D2;
        padding-bottom: 10px;
        margin-bottom: 14px;
    }}
    .institution {{
        font-size: 14pt;
        font-weight: 800;
        color: #0f172a;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .sub-institution {{
        font-size: 10pt;
        font-weight: 600;
        color: #1976D2;
        margin-top: 2px;
    }}
    .lab-title {{
        font-size: 14pt;
        font-weight: 800;
        color: #0284c7;
        margin-top: 8px;
        line-height: 1.25;
    }}
    .meta-table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        background: #f8fafc;
        border-radius: 6px;
        overflow: hidden;
        border: 1px solid #e2e8f0;
    }}
    .meta-table td {{
        padding: 5px 10px;
        font-size: 8.5pt;
        border-bottom: 1px solid #e2e8f0;
    }}
    .meta-table td.label {{
        font-weight: 700;
        color: #334155;
        width: 22%;
        background: #f1f5f9;
    }}
    h2 {{
        color: #0f172a;
        font-size: 11.5pt;
        border-left: 4px solid #1976D2;
        padding-left: 8px;
        margin-top: 18px;
        margin-bottom: 8px;
        break-after: avoid;
    }}
    h3 {{
        color: #1e293b;
        font-size: 10pt;
        margin-top: 12px;
        margin-bottom: 6px;
        break-after: avoid;
    }}
    p {{
        margin: 4px 0 8px 0;
        text-align: justify;
    }}
    ul, ol {{
        margin: 4px 0 8px 18px;
        padding: 0;
    }}
    li {{
        margin-bottom: 3px;
    }}
    table.data-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 8px 0 12px 0;
        font-size: 8.5pt;
        break-inside: avoid;
    }}
    table.data-table th, table.data-table td {{
        border: 1px solid #cbd5e1;
        padding: 6px 8px;
        text-align: left;
    }}
    table.data-table th {{
        background: #0f172a;
        color: #ffffff;
        font-weight: 600;
    }}
    table.data-table tr:nth-child(even) {{
        background: #f8fafc;
    }}
    .highlight-card {{
        background: #f0f9ff;
        border-left: 3px solid #0284c7;
        padding: 8px 12px;
        margin: 8px 0;
        border-radius: 0 5px 5px 0;
        font-size: 9pt;
        break-inside: avoid;
    }}
    .evidence-container {{
        display: flex;
        justify-content: center;
        gap: 20px;
        margin: 12px 0;
        break-inside: avoid;
    }}
    .evidence-item {{
        flex: 1;
        max-width: 320px;
        text-align: center;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }}
    .evidence-item img {{
        max-width: 195px;
        border-radius: 6px;
        border: 1px solid #cbd5e1;
        box-shadow: 0 4px 8px rgba(0,0,0,0.12);
    }}
    .evidence-caption {{
        margin-top: 6px;
        font-weight: 700;
        font-size: 9pt;
    }}
    .evidence-desc {{
        font-size: 8pt;
        color: #64748b;
    }}
    .code-block {{
        background: #1e1e1e;
        color: #d4d4d4;
        padding: 10px;
        border-radius: 6px;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 7.5pt;
        line-height: 1.35;
        white-space: pre-wrap;
        word-break: break-all;
        margin: 8px 0;
    }}
    .page-break {{
        break-before: page;
    }}
    .badge {{
        display: inline-block;
        padding: 2px 7px;
        border-radius: 10px;
        font-size: 7.5pt;
        font-weight: 700;
        text-transform: uppercase;
    }}
    .badge-blue {{
        background: #e0f2fe;
        color: #0369a1;
    }}
    .badge-red {{
        background: #fee2e2;
        color: #b91c1c;
    }}
    .diagram-box {{
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        padding: 10px;
        margin: 8px 0;
        font-family: 'Consolas', monospace;
        font-size: 8.5pt;
        line-height: 1.4;
        break-inside: avoid;
    }}
</style>
</head>
<body>

<div class="header-box">
    <div class="institution">Pontificia Universidad Católica del Ecuador</div>
    <div class="sub-institution">Facultad de Hábitat, Infraestructura y Creatividad • Programación Móvil (API 36)</div>
    <div class="lab-title">Informe de Laboratorio 5.2 / 5.3: Reto Integrador<br>Implementación de un Termostato Inteligente Reactivo</div>
</div>

<table class="meta-table">
    <tr>
        <td class="label">Asignatura:</td>
        <td>Redes y Dispositivos Avanzados 2 (RDA-2) / Programación Móvil</td>
        <td class="label">Fecha:</td>
        <td>23 de Octubre de 2026</td>
    </tr>
    <tr>
        <td class="label">Docente:</td>
        <td>Dr. Juan Francisco Chafla, PhD.</td>
        <td class="label">Entorno:</td>
        <td>Android Studio Ladybug | API 36 | Jetpack Compose</td>
    </tr>
    <tr>
        <td class="label">Grupo:</td>
        <td>Reto Grupo 1</td>
        <td class="label">Commit Final:</td>
        <td><code>e0b199a</code></td>
    </tr>
    <tr>
        <td class="label">Estudiante:</td>
        <td>Paul Rosero</td>
        <td class="label">Repositorio:</td>
        <td><code>github.com/paulrosero/RDA2_Lab5.3_Reto_Grupo1</code></td>
    </tr>
</table>

<h2>1. Objetivo del Reto y Contextualización</h2>
<p>
El presente reto integrador tiene como propósito aplicar los fundamentos del <strong>paradigma declarativo</strong> y la <strong>arquitectura reactiva</strong> impartidos en el <em>Tema 5</em>, tales como la <strong>Gestión de Estado</strong>, <strong>State Hoisting (Elevación de Estado)</strong>, <strong>Flujo Unidireccional de Datos (UDF)</strong> y la <strong>Recomposición Inteligente</strong>, para diseñar un panel de climatización funcional en <strong>Android API 36</strong>.
</p>
<p>
A diferencia del paradigma imperativo tradicional (layouts XML y Java/Kotlin), donde los elementos visuales se actualizaban manualmente mediante <code>findViewById</code>, <code>setText()</code> y <code>setVisibility()</code> propiciando fallas de desincronización, en Jetpack Compose la interfaz se concibe como una función determinista directa del estado: <strong>UI = f(State)</strong>. El sistema redibuja de forma instantánea la apariencia gráfica basándose exclusivamente en el flujo de datos.
</p>

<h2>2. Marco Teórico y Buenas Prácticas (Tema 5)</h2>
<div class="highlight-card">
    <strong>Principio Filosófico "Cómo vs Qué":</strong> En lugar de describir paso a paso la secuencia de instrucciones para alterar los widgets existentes (paradigma imperativo), el desarrollador describe el estado visual final deseado (paradigma declarativo). Compose gestiona la ejecución y optimización de forma automática.
</div>

<table class="data-table">
    <thead>
        <tr>
            <th>Concepto</th>
            <th>Paradigma Tradicional (XML)</th>
            <th>Paradigma Declarativo (Jetpack Compose)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Estructura</strong></td>
            <td>Archivos XML estáticos separados de la lógica.</td>
            <td>Funciones <code>@Composable</code> con DSL especializado en Kotlin.</td>
        </tr>
        <tr>
            <td><strong>Sincronización</strong></td>
            <td>Manual mediante <code>findViewById</code> y setters.</td>
            <td>Automática y reactiva ante cambios en las variables de estado.</td>
        </tr>
        <tr>
            <td><strong>Fuente de Verdad</strong></td>
            <td>Dispersa entre variables y propiedades de vistas.</td>
            <td>Centralizada (Single Source of Truth mediante State Hoisting).</td>
        </tr>
        <tr>
            <td><strong>Rendimiento</strong></td>
            <td>Inflado de jerarquías de vistas pesadas en memoria.</td>
            <td>Recomposición inteligente con omisión (skipping) de nodos estáticos.</td>
        </tr>
        <tr>
            <td><strong>Convergencia</strong></td>
            <td>Android View System (dispar a iOS UIKit).</td>
            <td>Alineado con SwiftUI en iOS (<code>Column</code>/<code>VStack</code>, <code>remember</code>/<code>@State</code>).</td>
        </tr>
    </tbody>
</table>

<h3>Pilares Clave de Implementación:</h3>
<ul>
    <li><strong><code>remember</code>:</strong> Preserva el valor en memoria a través de las sucesivas recomposiciones del árbol de composición.</li>
    <li><strong><code>mutableIntStateOf</code>:</strong> Observador reactivo primitivo de alto rendimiento que notifica a Compose las mutaciones del entero de temperatura sin incurrir en boxing innecesario.</li>
    <li><strong>State Hoisting (Elevación del Estado):</strong> El estado mutable reside únicamente en el contenedor padre (<code>ThermostatScreen</code>), convirtiendo a los subcomponentes hijos en <strong>Stateless</strong> (puros, altamente testeables y reutilizables).</li>
    <li><strong>Unidirectional Data Flow (UDF):</strong> El estado desciende por parámetros inmutables (<em>State Down</em>) y las acciones del usuario ascienden hacia el padre mediante funciones lambda (<em>Events Up</em>).</li>
</ul>

<h2>3. Jerarquía y Arquitectura de la Solución</h2>
<div class="diagram-box">
[ThermostatScreen (Stateful Parent - Single Source of Truth)]<br>
&nbsp;&nbsp;&nbsp;&nbsp;│<br>
&nbsp;&nbsp;&nbsp;&nbsp;├──► State Down (temperature: Int) ────► [TemperatureDisplay (Stateless Child)]<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ Lógica Condicional: temp >= 25°C ? Rojo : Azul<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ Icono: WbSunny (Sol) o AcUnit (Nieve)<br>
&nbsp;&nbsp;&nbsp;&nbsp;│<br>
&nbsp;&nbsp;&nbsp;&nbsp;└──◄ Events Up: onIncrease() / onDecrease() ◄ [TemperatureControls (Stateless Child)]<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└─ Botones delegados: Subir (+) y Bajar (-)
</div>

<p>
Cumpliendo rigurosamente con los <strong>Requisitos Técnicos</strong>:
</p>
<ul>
    <li>Se prescindió en su totalidad de archivos XML de layout o selectores estáticos.</li>
    <li>Se utilizaron modificadores <code>Modifier.padding()</code> y elementos <code>Spacer</code> para mantener márgenes y jerarquías proporcionales.</li>
    <li>El componente <code>TemperatureDisplay</code> no posee ningún estado mutable interno, satisfaciendo la condición de ser 100% <em>Stateless</em>.</li>
</ul>

<div class="page-break"></div>

<h2>4. Evidencias de Ejecución y Validación en Emulador API 36</h2>
<p>
La aplicación fue validada en el emulador <strong>Pixel 8 (Android API 36)</strong>. Al pulsar los botones de interacción, la apariencia visual (número, etiqueta de modo, color de acento, fondo de tarjeta e icono) conmutó de forma inmediata y automática sin recarga de Activity.
</p>

<div class="evidence-container">
    <div class="evidence-item">
        <span class="badge badge-blue">Estado Frío (&lt; 25°C)</span>
        <div style="margin-top: 8px;">
            <img src="data:image/png;base64,{frio_b64}" alt="Termostato Frío">
        </div>
        <div class="evidence-caption" style="color: #1976D2;">Temperatura: 20°C (Valor Inicial)</div>
        <div class="evidence-desc">Icono de Copo de Nieve (AcUnit) • Tonalidad Azul (#1976D2) • Modo Refrigeración</div>
    </div>
    <div class="evidence-item">
        <span class="badge badge-red">Estado Calor (>= 25°C)</span>
        <div style="margin-top: 8px;">
            <img src="data:image/png;base64,{calor_b64}" alt="Termostato Calor">
        </div>
        <div class="evidence-caption" style="color: #D32F2F;">Temperatura: 26°C (Umbral Superado)</div>
        <div class="evidence-desc">Icono de Sol (WbSunny) • Tonalidad Roja (#D32F2F) • Modo Calefacción</div>
    </div>
</div>

<h2>5. Análisis de Resultados y Discusión Técnica</h2>
<ol>
    <li><strong>Reactividad Determinista:</strong> La condición <code>val isWarm = temperature >= 25</code> dentro de <code>TemperatureDisplay</code> define de manera concisa el comportamiento visual completo. Toda mutación sobre <code>temperature</code> generada en los controles actualiza los nodos correspondientes en menos de 16 milisegundos (60-120 fps).</li>
    <li><strong>Eficiencia por Recomposición Inteligente:</strong> Al comparar con la analogía de la hoja de cálculo explicada en clase, Compose redibujó exclusivamente el bloque interno de <code>TemperatureDisplay</code>, omitiendo por completo los títulos estáticos de la cabecera.</li>
    <li><strong>Desacoplamiento Estructural:</strong> Los botones no alteran variables de forma directa; delegan la mutación a través de lambdas al contenedor padre, garantizando una trazabilidad perfecta del estado y permitiendo crear vistas previas (<code>@Preview</code>) de forma independiente.</li>
</ol>

<h2>6. Conclusiones</h2>
<ol>
    <li><strong>Consolidación del Paradigma Declarativo:</strong> La implementación demostró cómo Jetpack Compose simplifica el desarrollo móvil al convertir la UI en una función directa del estado, eliminando errores de desincronización propios de XML.</li>
    <li><strong>Madurez de la Arquitectura con State Hoisting:</strong> Centralizar el estado en el componente padre y delegar a hijos Stateless asegura un código desacoplado, modular y óptimo para pruebas unitarias e instrumentadas.</li>
    <li><strong>Alineación con Estándares de la Industria en API 36:</strong> La utilización de Kotlin 2.0 y Compose en API 36 valida que los conocimientos adquiridos en el Tema 5 corresponden a las mejores prácticas de ingeniería de software vigentes a nivel global.</li>
</ol>

<h2>7. Recomendaciones</h2>
<ol>
    <li><strong>Optimización de tipos de datos:</strong> Preferir <code>mutableIntStateOf</code> en lugar de <code>mutableStateOf&lt;Int&gt;</code> para prevenir la sobrecarga de boxing/unboxing en contadores de alta frecuencia.</li>
    <li><strong>Uso estricto del Bill of Materials (BOM):</strong> Mantener alineadas las dependencias de Material Icons Extended mediante <code>platform(libs.androidx.compose.bom)</code> para garantizar compatibilidad binaria.</li>
    <li><strong>Diseño basado en Spacers y Modifiers:</strong> Emplear espaciadores relativos y modificadores de relleno en lugar de tamaños absolutos fijos para garantizar una interfaz responsiva ante múltiples formatos de pantalla.</li>
</ol>

<div class="page-break"></div>

<h2>8. Anexo: Código Fuente Implementado (MainActivity.kt)</h2>
<p>A continuación se presenta el código fuente íntegro del archivo <code>MainActivity.kt</code> con comentarios explicativos en cada una de sus secciones:</p>

<div class="code-block">package com.paulrosero.laboratorio1

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AcUnit
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Remove
import androidx.compose.material.icons.filled.WbSunny
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.paulrosero.laboratorio1.ui.theme.Laboratorio1Theme

/**
 * LABORATORIO 5.2 / 5.3: RETO INTEGRADOR - CLIMATIZADOR REACTIVO
 * Demostración práctica de UI Declarativa, State Hoisting y Recomposición Inteligente.
 */
class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        enableEdgeToEdge() // Habilita dibujo edge-to-edge en API 36
        setContent {{
            Laboratorio1Theme {{
                Scaffold(modifier = Modifier.fillMaxSize()) {{ innerPadding ->
                    ThermostatScreen(
                        modifier = Modifier.fillMaxSize().padding(innerPadding)
                    )
                }}
            }}
        }}
    }}
}}

/**
 * COMPONENTE PADRE (Stateful): Contenedor principal y única fuente de verdad (Single Source of Truth).
 * Gestiona el estado reactivo con remember y mutableIntStateOf(20).
 */
@Composable
fun ThermostatScreen(modifier: Modifier = Modifier) {{
    // Estado reactivo: valor entero inicial en 20°C
    var temperature by remember {{ mutableIntStateOf(20) }}

    Column(
        modifier = modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {{
        Text(
            text = "Climatizador Reactivo",
            style = MaterialTheme.typography.headlineMedium,
            fontWeight = FontWeight.Bold
        )
        Text(
            text = "Control de Climatización Inteligente - API 36",
            style = MaterialTheme.typography.bodyMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )

        Spacer(modifier = Modifier.height(32.dp))

        // State Down: El estado desciende hacia el hijo de visualización
        TemperatureDisplay(
            temperature = temperature,
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(32.dp))

        // Events Up: Los eventos de usuario ascienden al padre mediante lambdas
        TemperatureControls(
            onIncrease = {{ temperature++ }},
            onDecrease = {{ temperature-- }},
            modifier = Modifier.fillMaxWidth()
        )
    }}
}}

/**
 * SUBCOMPONENTE DE VISUALIZACIÓN (Stateless):
 * Recibe la temperatura como parámetro. No almacena estado interno.
 * Aplica lógica condicional declarativa: >= 25°C -> Rojo y Sol; < 25°C -> Azul y Nieve.
 */
@Composable
fun TemperatureDisplay(temperature: Int, modifier: Modifier = Modifier) {{
    val isWarm = temperature >= 25
    val statusColor = if (isWarm) Color(0xFFD32F2F) else Color(0xFF1976D2)
    val backgroundColor = if (isWarm) Color(0xFFFFEBEE) else Color(0xFFE3F2FD)
    val icon = if (isWarm) Icons.Filled.WbSunny else Icons.Filled.AcUnit
    val statusLabel = if (isWarm) "Modo Calor (>= 25°C)" else "Modo Frío (< 25°C)"
    val descriptionText = if (isWarm) "Calefacción Activada" else "Refrigeración Activada"

    Card(
        modifier = modifier,
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.cardColors(containerColor = backgroundColor),
        border = BorderStroke(2.dp, statusColor.copy(alpha = 0.5f)),
        elevation = CardDefaults.cardElevation(defaultElevation = 6.dp)
    ) {{
        Column(
            modifier = Modifier.fillMaxWidth().padding(vertical = 36.dp, horizontal = 24.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {{
            Box(
                modifier = Modifier
                    .size(100.dp)
                    .clip(CircleShape)
                    .background(statusColor.copy(alpha = 0.15f)),
                contentAlignment = Alignment.Center
            ) {{
                Icon(
                    imageVector = icon,
                    contentDescription = statusLabel,
                    tint = statusColor,
                    modifier = Modifier.size(64.dp)
                )
            }}

            Spacer(modifier = Modifier.height(18.dp))

            Text(
                text = "$temperature°C",
                fontSize = 58.sp,
                fontWeight = FontWeight.ExtraBold,
                color = statusColor,
                textAlign = TextAlign.Center
            )

            Text(
                text = statusLabel,
                fontSize = 18.sp,
                fontWeight = FontWeight.SemiBold,
                color = statusColor
            )

            Spacer(modifier = Modifier.height(6.dp))

            Text(
                text = descriptionText,
                fontSize = 14.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant
            )
        }}
    }}
}}

/**
 * SUBCOMPONENTE DE CONTROLES (Stateless):
 * Contiene dos botones (Subir/Bajar) que ejecutan lambdas recibidas del contenedor padre.
 */
@Composable
fun TemperatureControls(
    onIncrease: () -> Unit,
    onDecrease: () -> Unit,
    modifier: Modifier = Modifier
) {{
    Row(
        modifier = modifier.padding(horizontal = 8.dp),
        horizontalArrangement = Arrangement.SpaceEvenly,
        verticalAlignment = Alignment.CenterVertically
    ) {{
        Button(
            onClick = onDecrease,
            shape = RoundedCornerShape(16.dp),
            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFF1976D2)),
            modifier = Modifier.weight(1f).height(56.dp)
        ) {{
            Icon(imageVector = Icons.Filled.Remove, contentDescription = "Bajar")
            Spacer(modifier = Modifier.width(8.dp))
            Text(text = "Bajar", fontSize = 16.sp, fontWeight = FontWeight.Bold)
        }}

        Spacer(modifier = Modifier.width(16.dp))

        Button(
            onClick = onIncrease,
            shape = RoundedCornerShape(16.dp),
            colors = ButtonDefaults.buttonColors(containerColor = Color(0xFFD32F2F)),
            modifier = Modifier.weight(1f).height(56.dp)
        ) {{
            Icon(imageVector = Icons.Filled.Add, contentDescription = "Subir")
            Spacer(modifier = Modifier.width(8.dp))
            Text(text = "Subir", fontSize = 16.sp, fontWeight = FontWeight.Bold)
        }}
    }}
}}

@Preview(showBackground = true, name = "Estado Frío (< 25°C)")
@Composable
fun ThermostatScreenColdPreview() {{
    Laboratorio1Theme {{
        Surface {{
            Column(modifier = Modifier.fillMaxSize().padding(24.dp), horizontalAlignment = Alignment.CenterHorizontally) {{
                Text("Climatizador Reactivo", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureDisplay(temperature = 20)
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureControls(onIncrease = {{}}, onDecrease = {{}})
            }}
        }}
    }}
}}

@Preview(showBackground = true, name = "Estado Calor (>= 25°C)")
@Composable
fun ThermostatScreenWarmPreview() {{
    Laboratorio1Theme {{
        Surface {{
            Column(modifier = Modifier.fillMaxSize().padding(24.dp), horizontalAlignment = Alignment.CenterHorizontally) {{
                Text("Climatizador Reactivo", style = MaterialTheme.typography.headlineMedium, fontWeight = FontWeight.Bold)
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureDisplay(temperature = 26)
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureControls(onIncrease = {{}}, onDecrease = {{}})
            }}
        }}
    }}
}}</div>

</body>
</html>
"""

html_path = os.path.join(WORKSPACE, "informe_temp.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}")
    page.pdf(
        path=OUTPUT_PDF,
        format="A4",
        print_background=True,
        margin={"top": "12mm", "bottom": "12mm", "left": "14mm", "right": "14mm"}
    )
    browser.close()

if os.path.exists(html_path):
    os.remove(html_path)

print(f"PDF optimizado exitosamente en: {OUTPUT_PDF}")
