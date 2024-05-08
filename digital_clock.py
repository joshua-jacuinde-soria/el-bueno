class Digital_clock:
    def __init__(self, h:int = 23, m: int = 58, s: int = 0) -> None:
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
        """incremento de un segundo en tiempo concurrente
        """
        self.__h = self.__h + 1 if self.__m ==59 and self.__s == 59 else self.__h
        self.__h = 0 if self.__h == 24 else self.__h
        self.__m = self.__m + 1 if self.__s == 59 else self.__m
        self.__m = 0 if self.__m == 60 else self.__m
        self.__s = self.__s + 1 if self.__s < 59 else 0
    