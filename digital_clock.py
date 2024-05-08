class Digital_clock:
    def __init__(self, h:int = 0, m: int = 0, s: int = 0) -> None:
        """Contrtuctor

        Args:
            h (int, optional): contador de horas. Defaults to 0.
            m (int, optional): contador de minutos. Defaults to 0.
            s (int, optional): contador de segundos. Defaults to 0.
        """ 
        assert h < 24 and h >= 0
        self.__h = h
        assert m < 60 and m >= 0
        self.__m = m
        assert s < 60 and s >= 0
        self.__s = s
    
    def get_time(self)->tuple[int, int, int]:
        """regresa el tiempo de reloj

        Returns:
            tuple[int, int, int]: h,m,s in formato de 24 horas
        """
        return self.__h, self.__m, self.__s
    
    def clear_time(self):
        """limpia el tiempo
        """
        self.__h, self.__m, self.__m = 0, 0, 0
        
    def incremento(self):
        