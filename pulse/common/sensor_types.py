class SensorsPack:
    class Sensor(object):
        def __init__(self, names, label, barriers_count, available_barriers_to_calculate):
            self.names = set(names)
            self.alias = names[0]
            self.barriers_count = barriers_count
            self._label = label
            self.available_barriers_to_calculate = available_barriers_to_calculate

        def __str__(self):
            return self.alias

        def label(self):
            return self._label

        def get_barriers_count(self):
            return self.barriers_count

        def get_available_barriers(self):
            return self.available_barriers_to_calculate

        def __eq__(self, other):
            return True if str(other).upper() in self.names else False

        def __hash__(self):
            return str(self).__hash__()

    def __init__(self):
        self.PULSE_2_1 = SensorsPack.Sensor(
            ['SHORT',   'EMPULSE_2M_1', 'SS'],
            'Pulse 2 Short',
            barriers_count=2,
            available_barriers_to_calculate={0, },
        )
        self.PULSE_2_2 = SensorsPack.Sensor(
            ['MEDIUM',  'EMPULSE_2M_2', 'MS', 'LS'],
            'Pulse 2 Medium',
            barriers_count=3,
            available_barriers_to_calculate={0, 1, },
        )
        self.PULSE_3D_1 = SensorsPack.Sensor(
            ['LONG',    'EMPULSE_3D_1', 'VLS'],
            'Pulse 3D',
            barriers_count=3,
            available_barriers_to_calculate={0, 1, 2, },
        )
        self.PULSE_4_1 = SensorsPack.Sensor(
            ['LONGM',   'EMPULSE_4_1', 'EMPULSE_3M_1'],
            'Pulse 4',
            barriers_count=4,
            available_barriers_to_calculate={1, 2, 3, },
        )
        self.PULSE_3E_1 = SensorsPack.Sensor(
            ['3ESHORT', 'EMPULSE_3E_1'],
            'Pulse 3E Medium',
            barriers_count=3,
            available_barriers_to_calculate={0, 1, },
        )
        self.PULSE_3E_2 = SensorsPack.Sensor(
            ['3ELONG',  'EMPULSE_3E_2'],
            'Pulse 3E Long',
            barriers_count=3,
            available_barriers_to_calculate={0, 1, 2, },
        )
        self.PULSE_360_1 = SensorsPack.Sensor(
            ['P360_RS', 'EMPULSE_360_1', 'RS AGGREGATED', 'RS'],
            'Pulse 360 Radial',
            barriers_count=2,
            available_barriers_to_calculate={0, },
        )

    def __call__(self, sensor_name):
        for sensor in self.__dict__.keys():
            current_sensor = getattr(self, sensor)
            if sensor_name == current_sensor:
                return current_sensor


sensors = SensorsPack()


if __name__ == '__main__':
    print(sensors.PULSE_2_1 == 'EMPULSE_2M_1')
    print(sensors.PULSE_2_1 == sensors.PULSE_2_2, end='\n\n')

    current = sensors.PULSE_2_1
    print(current)
    print(current.get_barriers_count())
    print(current.label(), end='\n\n')

    print(sensors('EMPULSE_3D_1'))


pass
