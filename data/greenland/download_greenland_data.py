import sys
import os
src_directory = '../../'
sys.path.append(src_directory)

from src.helper import download_file


def convert_measures_projection(direc, var):
  """
  convert the measures .tif files to _new.tif files with the projection we 
  require using gdalwarp.
  """
  proj    = '\"+units=m  +proj=stere +lat_0=90 +lat_ts=71 +lon_0=-39 +k=1 ' \
            + '+x_0=0 +y_0=0 +no_defs +a=6378137 +rf=298.257223563 ' \
            + '+towgs84=0.000,0.000,0.000 +to_meter=1\"'
  te      = '-645000.0 -3370000.0 860000.0 -640000.0'
  infile  = direc + '/greenland_vel_mosaic500_2008_2009_' + var + '.tif'
  outfile = direc + '/greenland_vel_mosaic500_2008_2009_' + var + '_new.tif'

  cmd = 'gdalwarp ' + infile + ' ' + outfile + ' -t_srs ' + proj + ' -te ' + te
  
  print "\nExecuting :\n\n\t", cmd, "\n\n"
  os.system(cmd)


#===============================================================================
home = os.getcwd()

# measures velocity dataset :
fldr = 'measures'
meas = 'ftp://sidads.colorado.edu/pub/DATASETS/' + \
       'nsidc0478_MEASURES_greenland_V01/2008/' + \
       'greenland_vel_mosaic500_2008_2009'
download_file(meas + '_sp.tif', home, fldr)
download_file(meas + '_vx.tif', home, fldr)
download_file(meas + '_vy.tif', home, fldr)

# get errors in .tif format
errors  = 'https://dl.dropboxusercontent.com/s/65q1wtc8mofotnz/' +\
          'greenland_measures_error.tar.gz?dl=1&token_hash=AAEp' +\
          '-BIqyJTzkCTmUg-1hAtfU0iZYDqlkww5Oo5qgc0mTQ'
download_file(errors, home, fldr, extract=True)

# convert to searise projection via raster warp :
convert_measures_projection(home + '/' + fldr, 'vx')
convert_measures_projection(home + '/' + fldr, 'vy')
convert_measures_projection(home + '/' + fldr, 'ex')
convert_measures_projection(home + '/' + fldr, 'ey')
convert_measures_projection(home + '/' + fldr, 'sp')

# Fox Maule et al. (2005) basal heat flux :
q_geo   = 'http://websrv.cs.umt.edu/isis/images/d/da/Greenland_heat_flux_5km.nc'
fldr    = 'fox_maule'
download_file(q_geo, home, fldr)

# searise dataset :
searise = 'http://websrv.cs.umt.edu/isis/images/e/e9/Greenland_5km_dev1.2.nc'
fldr    = 'searise'
download_file(searise, home, fldr)

# smooth target matlab matrix :
smooth  = 'https://dl.dropboxusercontent.com/s/e8r0x37mil03hvu/' +\
          'smooth_target.tar.gz?dl=1&token_hash=AAGafyrXdL72vZL' +\
          'ffoBX3_kfAcEzvFhvrw8rERNx2WQShA'
fldr    = 'searise'
download_file(smooth, home, fldr, extract=True)

# Bamber 2013 bedrock topography dataset :
v2      = 'https://dl.dropboxusercontent.com/s/qd02y99d1xrkdz3/' + \
          'Greenland_bedrock_topography_V2.tar.gz?dl=1&token_ha' + \
          'sh=AAFzWa8fuvcKC2tBYqY9VzDLctRWwqX2EuN-179bJ74XEg'
fldr    = 'bamber13'
download_file(v2, home, fldr, extract=True)

# merged 2014 velocity data :
merged  = 'https://dl.dropboxusercontent.com/s/d50xn9nwr107awv/' + \
          'velocity_greenland_merged_15Feb2013.tar.gz?dl=1&toke' + \
          'n_hash=AAHz4wSf4OBzbVsVwwHvScaFTtADgTR6IO_siXZLh0BM9w'
fldr    = 'rignot'
download_file(merged, home, fldr, extract=True)


