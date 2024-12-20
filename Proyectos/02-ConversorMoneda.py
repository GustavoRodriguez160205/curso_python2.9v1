import streamlit as st

def convertir_moneda(cantidad, tasa_cambio):
        ## Función que hace la conversión
    return cantidad * tasa_cambio

def app():
   
    # Titulo
    st.write("Bienvenido al conversor de monedas. Selecciona las opciones y realiza la conversión.")

    opcion = st.radio("Elige una opción", ("USD a EUR", "EUR a USD"))

    if opcion == "USD a EUR":
        cantidad = st.number_input("Ingresa la cantidad en USD", min_value=0.01, step=0.01)
        if cantidad > 0 and st.button("Convertir 🚀"):
            tasa_cambio = 0.85 # Realizamos la conversión 
            resultado = convertir_moneda(cantidad, tasa_cambio)
            st.success(f"{cantidad} USD son {resultado:.2f} EUR")

            # Condiciónal para guardar los datos en el historial
            if 'historial' not in st.session_state:
                st.session_state.historial = []
            st.session_state.historial.append(f"{cantidad} USD -> {resultado:.2f} EUR")

    elif opcion == "EUR a USD":
        cantidad = st.number_input("Ingresa la cantidad en EUR", min_value=0.01, step=0.01)
        if cantidad > 0 and st.button("Convertir 🚀"):
            tasa_cambio = 1.18 
            resultado = convertir_moneda(cantidad, tasa_cambio)
            st.success(f"{cantidad} EUR son {resultado:.2f} USD")
           
            if 'historial' not in st.session_state:
                st.session_state.historial = []
            st.session_state.historial.append(f"{cantidad} EUR -> {resultado:.2f} USD")


    if 'historial' in st.session_state:
        st.write("Historial de conversiones:")
        for item in st.session_state.historial:
            st.write(item)

if __name__ == "__main__":
    app()
