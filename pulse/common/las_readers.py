import datetime
import lasio
import numpy as np
from .depth_units import DepthUnits
from dataclasses import dataclass
from typing import Dict, List, Tuple


def get_delta_depth(depths: np.ndarray) -> float:
    return np.diff(depths[:2]).item()


def load_las(filename: str, depth_range: Tuple[float, float]) -> Tuple[np.ndarray, np.ndarray, DepthUnits]:
    las = lasio.read(filename)
    depth_key = 'DEPT' if 'DEPT' in las.keys() else 'DEPTH'
    units = DepthUnits.M if las.curves[depth_key].unit.lower() == 'm' else DepthUnits.FT
    depths = las.curves[depth_key].data
    mask = np.logical_and(depths < depth_range[1], depths > depth_range[0])
    return depths[mask], las.data[mask, 1:], units


def load_las_by_curve_name(
    filename: str, curve_names: List[str], depth_range: Tuple[float, float]
) -> Tuple[np.ndarray, np.ndarray, DepthUnits]:
    las = lasio.read(filename)
    depth_key = 'DEPT' if 'DEPT' in las.keys() else 'DEPTH'
    units = DepthUnits.M if las.curves[depth_key].unit.lower() == 'm' else DepthUnits.FT
    depths = las.curves[depth_key].data
    mask = np.logical_and(depths < depth_range[1], depths > depth_range[0])
    curves = [las.curves[n].data[mask] for n in curve_names]
    return depths[mask], np.array(curves).T, units


def make_las(data_dict: Dict) -> lasio.LASFile:
    las_file = lasio.LASFile()
    las_file.well['DATE'].value = str(datetime.datetime.today())
    las_file.params['ENGI'] = lasio.HeaderItem('ENGI', '', 'test@test.com', 'Creator of this file...')
    las_file.other = 'LAS file using lasio'
    las_file.curves.clear()
    las_file.add_curve('DEPT', data_dict['DEPT'].values, unit=data_dict['DEPT'].units.alias or 'm')
    for key in data_dict.keys():
        if key != 'DEPT':
            las_file.add_curve(
                str(key), data_dict[key].values, unit=data_dict[key].units, descr='Example data',
            )
    return las_file


@dataclass
class LasLog:
    values: np.ndarray
    units: str = 'frac'


pass
