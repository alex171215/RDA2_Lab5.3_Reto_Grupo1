package com.paulrosero.laboratorio1

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.BorderStroke
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AcUnit
import androidx.compose.material.icons.filled.Add
import androidx.compose.material.icons.filled.Remove
import androidx.compose.material.icons.filled.WbSunny
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableIntStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
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
 * =========================================================================================
 * LABORATORIO 5.2 / 5.3: RETO INTEGRADOR - CLIMATIZADOR REACTIVO (TERMOSTATO INTELIGENTE)
 * =========================================================================================
 * 
 * Conceptos aplicados según el Tema 5:
 * 1. Paradigma Declarativo: La UI se define como una función directa del estado: UI = f(State).
 *    No se manipulan vistas imperativamente (prohibido findViewById, setText, setVisibility).
 * 2. State Hoisting (Elevación de Estado): El estado de la temperatura se mantiene en el
 *    componente padre (ThermostatScreen), haciendo que los subcomponentes hijos sean "Stateless"
 *    (reutilizables, predecibles y fáciles de testear).
 * 3. Flujo Unidireccional de Datos (UDF):
 *    - Hacia abajo (Down): El estado desciende hacia los componentes de presentación (TemperatureDisplay).
 *    - Hacia arriba (Up): Los eventos de interacción del usuario se propagan hacia el padre
 *      mediante funciones lambda (onIncrease / onDecrease).
 * 4. Recomposición Inteligente: Al mutar el estado con mutableIntStateOf, Compose redibuja
 *    únicamente los nodos del árbol de composición que dependen del valor de la temperatura,
 *    omitiendo los nodos estáticos (Skipping).
 */

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        // Habilita el soporte Edge-to-Edge para aprovechar la pantalla completa en API 36
        enableEdgeToEdge()
        setContent {
            Laboratorio1Theme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    // Invocamos el Composable principal pasando el padding del sistema
                    ThermostatScreen(
                        modifier = Modifier
                            .fillMaxSize()
                            .padding(innerPadding)
                    )
                }
            }
        }
    }
}

/**
 * COMPOSABLE PADRE: ThermostatScreen (Stateful)
 * -----------------------------------------------------------------------------------------
 * Cumple con el rol de contenedor principal y "Única Fuente de Verdad" (Single Source of Truth).
 * - Declara y almacena el estado reactivo de la temperatura con remember y mutableIntStateOf.
 * - Coordina la comunicación entre la visualización y los controles mediante State Hoisting.
 */
@Composable
fun ThermostatScreen(modifier: Modifier = Modifier) {
    // -------------------------------------------------------------------------------------
    // GESTIÓN DE ESTADO (Tema 5):
    // - remember: Conserva el valor en memoria a través de las recomposiciones del árbol de Compose.
    // - mutableIntStateOf(20): Observador reactivo primitivo optimizado para enteros. Inicializado en 20°C.
    //   Cualquier lectura de esta variable suscribe al composable a futuras recomposiciones.
    // -------------------------------------------------------------------------------------
    var temperature by remember { mutableIntStateOf(20) }

    Column(
        modifier = modifier
            .fillMaxSize()
            .background(MaterialTheme.colorScheme.background)
            .padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        // Título del sistema con tipografía moderna y espaciado
        Text(
            text = "Climatizador Reactivo",
            style = MaterialTheme.typography.headlineMedium,
            fontWeight = FontWeight.Bold,
            color = MaterialTheme.colorScheme.onBackground
        )

        Text(
            text = "Control de Climatización Inteligente - API 36",
            style = MaterialTheme.typography.bodyMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant
        )

        // Separador estructural vertical
        Spacer(modifier = Modifier.height(32.dp))

        // ---------------------------------------------------------------------------------
        // SUBCOMPONENTE HIJO 1: Visualización (Stateless)
        // El estado desciende (State Down) mediante el parámetro 'temperature'.
        // ---------------------------------------------------------------------------------
        TemperatureDisplay(
            temperature = temperature,
            modifier = Modifier.fillMaxWidth()
        )

        // Separador estructural vertical
        Spacer(modifier = Modifier.height(32.dp))

        // ---------------------------------------------------------------------------------
        // SUBCOMPONENTE HIJO 2: Controles (Stateless)
        // Los eventos ascienden (Events Up) ejecutando las lambdas emitidas por el padre.
        // El hijo no contiene lógica de negocio ni muta variables por su cuenta.
        // ---------------------------------------------------------------------------------
        TemperatureControls(
            onIncrease = {
                // Lambda para incrementar la temperatura
                temperature++
            },
            onDecrease = {
                // Lambda para decrementar la temperatura
                temperature--
            },
            modifier = Modifier.fillMaxWidth()
        )
    }
}

/**
 * SUBCOMPONENTE HIJO 1: TemperatureDisplay (Stateless)
 * -----------------------------------------------------------------------------------------
 * Componente libre de estado interno. Cumple con la especificación de diseño:
 * - Recibe únicamente 'temperature' y 'modifier' por parámetros.
 * - Lógica Declarativa Condicional:
 *   * Si temperature >= 25°C: Color Rojo e Icono de Sol (WbSunny).
 *   * Si temperature < 25°C: Color Azul e Icono de Copo de Nieve (AcUnit).
 * - Se redibuja de forma instantánea y reactiva sin recrear la Activity.
 */
@Composable
fun TemperatureDisplay(
    temperature: Int,
    modifier: Modifier = Modifier
) {
    // -------------------------------------------------------------------------------------
    // LÓGICA DECLARATIVA CONDICIONAL (UI = f(State)):
    // Se calculan las propiedades visuales en función directa del estado recibido.
    // -------------------------------------------------------------------------------------
    val isWarm = temperature >= 25

    // Colores temáticos armonizados según el reto
    val statusColor = if (isWarm) Color(0xFFD32F2F) else Color(0xFF1976D2) // Rojo vibrante / Azul fresco
    val backgroundColor = if (isWarm) Color(0xFFFFEBEE) else Color(0xFFE3F2FD) // Fondos suaves contrastantes
    val icon = if (isWarm) Icons.Filled.WbSunny else Icons.Filled.AcUnit
    val statusLabel = if (isWarm) "Modo Calor (>= 25°C)" else "Modo Frío (< 25°C)"
    val descriptionText = if (isWarm) "Calefacción Activada" else "Refrigeración Activada"

    // Tarjeta contenedora con esquinas redondeadas y elevación suave
    Card(
        modifier = modifier,
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.cardColors(containerColor = backgroundColor),
        border = BorderStroke(2.dp, statusColor.copy(alpha = 0.5f)),
        elevation = CardDefaults.cardElevation(defaultElevation = 6.dp)
    ) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .padding(vertical = 36.dp, horizontal = 24.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {
            // Contenedor circular con efecto de halo para el icono
            Box(
                modifier = Modifier
                    .size(100.dp)
                    .clip(CircleShape)
                    .background(statusColor.copy(alpha = 0.15f)),
                contentAlignment = Alignment.Center
            ) {
                Icon(
                    imageVector = icon,
                    contentDescription = statusLabel,
                    tint = statusColor,
                    modifier = Modifier.size(64.dp)
                )
            }

            // Espaciado estructural
            Spacer(modifier = Modifier.height(18.dp))

            // Indicador numérico principal de la temperatura
            Text(
                text = "$temperature°C",
                fontSize = 58.sp,
                fontWeight = FontWeight.ExtraBold,
                color = statusColor,
                textAlign = TextAlign.Center
            )

            // Etiqueta del modo operativo
            Text(
                text = statusLabel,
                fontSize = 18.sp,
                fontWeight = FontWeight.SemiBold,
                color = statusColor,
                textAlign = TextAlign.Center
            )

            // Espaciado estructural
            Spacer(modifier = Modifier.height(6.dp))

            // Subtexto descriptivo del estado
            Text(
                text = descriptionText,
                fontSize = 14.sp,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                textAlign = TextAlign.Center
            )
        }
    }
}

/**
 * SUBCOMPONENTE HIJO 2: TemperatureControls (Stateless)
 * -----------------------------------------------------------------------------------------
 * Contenedor de botones para Subir y Bajar la temperatura.
 * - Es 100% Stateless: no posee variables de estado ni lógica de modificación propia.
 * - Delega la acción mediante funciones lambda de orden superior (onIncrease, onDecrease).
 * - Utiliza espaciadores (Spacer) y modificadores de relleno (padding) según la rúbrica.
 */
@Composable
fun TemperatureControls(
    onIncrease: () -> Unit,
    onDecrease: () -> Unit,
    modifier: Modifier = Modifier
) {
    Row(
        modifier = modifier.padding(horizontal = 8.dp),
        horizontalArrangement = Arrangement.SpaceEvenly,
        verticalAlignment = Alignment.CenterVertically
    ) {
        // Botón para Bajar la temperatura
        Button(
            onClick = onDecrease,
            shape = RoundedCornerShape(16.dp),
            colors = ButtonDefaults.buttonColors(
                containerColor = Color(0xFF1976D2), // Tonalidad azul coherente
                contentColor = Color.White
            ),
            modifier = Modifier
                .weight(1f)
                .height(56.dp)
        ) {
            Icon(
                imageVector = Icons.Filled.Remove,
                contentDescription = "Bajar Temperatura",
                modifier = Modifier.size(24.dp)
            )
            Spacer(modifier = Modifier.width(8.dp))
            Text(
                text = "Bajar",
                fontSize = 16.sp,
                fontWeight = FontWeight.Bold
            )
        }

        // Espaciador horizontal entre botones
        Spacer(modifier = Modifier.width(16.dp))

        // Botón para Subir la temperatura
        Button(
            onClick = onIncrease,
            shape = RoundedCornerShape(16.dp),
            colors = ButtonDefaults.buttonColors(
                containerColor = Color(0xFFD32F2F), // Tonalidad roja coherente
                contentColor = Color.White
            ),
            modifier = Modifier
                .weight(1f)
                .height(56.dp)
        ) {
            Icon(
                imageVector = Icons.Filled.Add,
                contentDescription = "Subir Temperatura",
                modifier = Modifier.size(24.dp)
            )
            Spacer(modifier = Modifier.width(8.dp))
            Text(
                text = "Subir",
                fontSize = 16.sp,
                fontWeight = FontWeight.Bold
            )
        }
    }
}

/**
 * =========================================================================================
 * PREVIEWS PARA ENTORNO DE DESARROLLO (Android Studio Ladybug)
 * Permite validar visualmente ambos estados declarativos sin necesidad de ejecutar la app.
 * =========================================================================================
 */

@Preview(showBackground = true, name = "Estado Frío (< 25°C)")
@Composable
fun ThermostatScreenColdPreview() {
    Laboratorio1Theme {
        Surface {
            // Previsualización estática del estado Frío (ej: 20°C por defecto)
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                Text(
                    text = "Climatizador Reactivo",
                    style = MaterialTheme.typography.headlineMedium,
                    fontWeight = FontWeight.Bold
                )
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureDisplay(temperature = 20)
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureControls(onIncrease = {}, onDecrease = {})
            }
        }
    }
}

@Preview(showBackground = true, name = "Estado Calor (>= 25°C)")
@Composable
fun ThermostatScreenWarmPreview() {
    Laboratorio1Theme {
        Surface {
            // Previsualización estática del estado Calor (ej: 26°C)
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                Text(
                    text = "Climatizador Reactivo",
                    style = MaterialTheme.typography.headlineMedium,
                    fontWeight = FontWeight.Bold
                )
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureDisplay(temperature = 26)
                Spacer(modifier = Modifier.height(32.dp))
                TemperatureControls(onIncrease = {}, onDecrease = {})
            }
        }
    }
}