class CuentaUsuario:

    # Atributos de clase 
    MAX_INTENTOS = 3
    dominio = "formacion.local"

    def __init__(self, nombre, email, password):
        """Crea una cuenta activa y sin intentos fallidos"""

        self.nombre = nombre                       
        self._email = email                        
        self.__password_hash = "hash_" + password  
        self._activa = True                        
        self._intentos_fallidos = 0                

    #Metodos consultores

    def esta_activa(self) -> bool:
        """Devuelve True si la cuenta está activa."""
        return self._activa

    def puede_iniciar_sesion(self) -> bool:
        """Devuelve True si está activa y no ha llegado al máximo de intentos."""
        return self._activa and self._intentos_fallidos < CuentaUsuario.MAX_INTENTOS

    def perfil_publico(self) -> str:
        """Devuelve un texto con los atributos públicos."""
        return "Nombre: " + self.nombre + " | Dominio: " + self.dominio

    def consultar_email(self) -> str:
        """Devuelve el email de la cuenta."""
        return self._email

    # Metodos modificadores

    def activar(self) -> None:
        """Activa la cuenta."""
        self._activa = True

    def desactivar(self) -> None:
        """Desactiva la cuenta."""
        self._activa = False

    def cambiar_email(self, nuevo_email: str) -> None:
        """Cambia el email si contiene @ y termina en el dominio de la clase."""
        if "@" not in nuevo_email:
            raise ValueError("El email debe contener @")
        if not nuevo_email.endswith(CuentaUsuario.dominio):
            raise ValueError("El email debe terminar en " + CuentaUsuario.dominio)
        self._email = nuevo_email

    def registrar_intento_fallido(self) -> None:
        """Suma un intento fallido y desactiva la cuenta si llega al máximo."""
        self._intentos_fallidos += 1
        if self._intentos_fallidos >= CuentaUsuario.MAX_INTENTOS:
            self._activa = False

    def reiniciar_intentos(self) -> None:
        """Pone a cero el contador de intentos fallidos."""
        self._intentos_fallidos = 0

#Main donde comprobamos el funcionamiento de nuestra clase 

def main(): 
    
    print("1. Crear dos cuentas")
    cuenta1 = CuentaUsuario("Ana", "ana@formacion.local", "1234")
    cuenta2 = CuentaUsuario("Luis", "luis@formacion.local", "abcd")
    print("Cuenta 1:", cuenta1.perfil_publico())
    print("Cuenta 2:", cuenta2.perfil_publico())

    print()
    print("2. Mostrar __dict__")
    print("cuenta1.__dict__:", cuenta1.__dict__)
    print("cuenta2.__dict__:", cuenta2.__dict__)

    print()
    print("=== 3. Son objetos distintos ===")
    print("cuenta1 is cuenta2:", cuenta1 is cuenta2)
    print("id(cuenta1):", id(cuenta1))
    print("id(cuenta2):", id(cuenta2))
    print("id(cuenta1) == id(cuenta2):", id(cuenta1) == id(cuenta2))
    print("type(cuenta1):", type(cuenta1))

    print()
    print("4. Enviar mensajes a los métodos")
    print("¿cuenta1 activa?", cuenta1.esta_activa())
    print("¿cuenta1 puede iniciar sesión?", cuenta1.puede_iniciar_sesion())
    print("Email de cuenta1:", cuenta1.consultar_email())
    cuenta1.cambiar_email("ana.nueva@formacion.local")
    print("Email nuevo de cuenta1:", cuenta1.consultar_email())
    try:
        cuenta1.cambiar_email("ana@gmail.com")
    except ValueError as error:
        print("Error controlado:", error)

    print()
    print("5. Modificar una cuenta no afecta a la otra")
    for i in range(CuentaUsuario.MAX_INTENTOS):
        cuenta1.registrar_intento_fallido()
        print("Intento fallido", i + 1, "- ¿cuenta1 activa?", cuenta1.esta_activa())
    print("cuenta1 puede iniciar sesión:", cuenta1.puede_iniciar_sesion())
    print("cuenta2 puede iniciar sesión:", cuenta2.puede_iniciar_sesion())
    print("cuenta2 sigue activa:", cuenta2.esta_activa())
    cuenta1.reiniciar_intentos()
    cuenta1.activar()
    print("Tras reiniciar y activar, cuenta1 puede iniciar sesión:",
          cuenta1.puede_iniciar_sesion())

    print()
    print("6. Atributo de clase")
    print("CuentaUsuario.MAX_INTENTOS:", CuentaUsuario.MAX_INTENTOS)
    print("cuenta1.MAX_INTENTOS:", cuenta1.MAX_INTENTOS)
    print("cuenta2.MAX_INTENTOS:", cuenta2.MAX_INTENTOS)
    print("'MAX_INTENTOS' en cuenta1.__dict__:", "MAX_INTENTOS" in cuenta1.__dict__)



if __name__ == "__main__":
    main()