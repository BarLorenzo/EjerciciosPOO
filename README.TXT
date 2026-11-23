# Práctica integradora RA1 (criterios a, b y c):

1. Explicación del modelo
La clase `CuentaUsuario` representa la cuenta de un usuario en una plataforma de formación.

Cada cuenta tiene:

- Estado: sus datos (nombre, email, password_hash, activa, intentos_fallidos)
- Comportamiento: sus métodos tanto de consulta como de modificacion (getters y setters)
- Identidad: cada cuenta es un objeto distinto, con su propio id

2. Ejemplos de ejecución
    1. Crear dos cuentas 
    Cuenta 1: Nombre: Ana | Dominio: formacion.local
    Cuenta 2: Nombre: Luis | Dominio: formacion.local

    2. Mostrar __dict__
    cuenta1.__dict__: {'nombre': 'Ana', '_email': 'ana@formacion.local', '_CuentaUsuario__password_hash': 'hash_1234', '_activa': True, '_intentos_fallidos': 0}
    cuenta2.__dict__: {'nombre': 'Luis', '_email': 'luis@formacion.local', '_CuentaUsuario__password_hash': 'hash_abcd', '_activa': True, '_intentos_fallidos': 0}

    3. Son objetos distintos
    cuenta1 is cuenta2: False
    id(cuenta1) == id(cuenta2): False

    5. Modificar una cuenta no afecta a la otra
    Intento fallido 3 - ¿cuenta1 activa? False
    cuenta1 puede iniciar sesión: False
    cuenta2 puede iniciar sesión: True

    6. Atributo privado y name mangling
    Acceso con name mangling: hash_1234


3. Diferencia entre atributos de instancia y de clase
Los atributos de instancia, pertenecen a cada objeto y cada uno tiene su propio valor. Se crea en __init__ con self mientras que los atributos de clase, pertenecen a la clase y lo comparten todas las instancias, se definen en el cuerpo de la clase

4. Diferencia entre consultor y modificador
Los consultores devuelven información del objeto y los modificadores cambian el estado del objeto

6. Reflexión sobre la visibilidad por convención
Python no tiene visibilidad real como Java, la visibilidad en Python se basa en la disciplina del programador y en ofrecer una buena interfaz: el código externo debe usar los métodos y no modificar directamente, para que la clase pueda validar los datos.