class FSM:
    """Esta clase pretende implementar una FSM determinista modelando ambos estados y eventos como integrantes
    """
    def __init__(self, estado_inicial: int = 0) -> None:
        """Este metodo inicializa al objeto FDM con el estado inicial

        Args:
            estado_inicial (int, optional): El estado inicial. Defaults to 0.
        """
        self.__estadoConcurrido: int = estado_inicial
        self.__reglas_transision: dict[tuple[int, int], int] = {}
        
    def obtener_estado_concurrido(self):
        
        """Obtiene el estado concurrido

            Returns:
                int: El estado concurrido de la FSM
        """
        return self.__estadoConcurrido
        
    def computar_siguiente_estado(self, ev:int):
        """Actualiza el codigo del estado concurrido acuerdo al siguiente estado

        Args:
            ev (int): El codigo de eventos que produce la transición
        """
        self.__estado_concurrido = self.__reglas_transision[(self.__estado_concurrido, ev)]
        
    def mandar_regla_transicion(self, estado_concurrido: int, numero_evento: int, siguiente_estado: int):
        """Manda una nueva regla de transición

        Args:
            estado_concurrido (int): EL codigo numerico del esatdo concurrido
            numero_evento (int): El codigo numerico del evento
            siguiente_estado (int): El codigo numerico del siguiete estado
        """
        self.__reglas_transision[(estado_concurrido, numero_evento)] = siguiente_estado