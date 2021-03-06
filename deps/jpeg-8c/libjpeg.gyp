# Copyright (c) 2009 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'conditions': [
      [ 'os_posix == 1 and OS != "mac"', {
        # Link to system .so since we already use it due to GTK.
        'use_system_libjpeg%': 1,
      }, {  # os_posix != 1 or OS == "mac"
        'use_system_libjpeg%': 0,
      }],
    ],
  },
  'conditions': [
    ['use_system_libjpeg==0', {
      'targets': [
        {
          'target_name': 'libjpeg',
          'type': 'static_library',
          'sources': [
            'jconfig.h',
            'jaricom.c',
            'jcapimin.c',
            'jcapistd.c',
            'jcarith.c',
            'jccoefct.c',
            'jccolor.c',
            'jcdctmgr.c',
            'jchuff.c',
            'jcinit.c',
            'jcmainct.c',
            'jcmarker.c',
            'jcmaster.c',
            'jcomapi.c',
            'jcparam.c',
            'jcprepct.c',
            'jcsample.c',
            'jctrans.c',
            'jdapimin.c',
            'jdapistd.c',
            'jdarith.c',
            'jdatadst.c',
            'jdatasrc.c',
            'jdcoefct.c',
            'jdcolor.c',
            'jdct.h',
            'jddctmgr.c',
            'jdhuff.c',
            'jdinput.c',
            'jdmainct.c',
            'jdmarker.c',
            'jdmaster.c',
            'jdmerge.c',
            'jdpostct.c',
            'jdsample.c',
            'jdtrans.c',
            'jerror.c',
            'jerror.h',
            'jfdctflt.c',
            'jfdctfst.c',
            'jfdctint.c',
            'jidctflt.c',
            'jidctfst.c',
            'jidctint.c',
            'jinclude.h',
            'jmemmgr.c',
            'jmemnobs.c',
            'jmemsys.h',
            'jmorecfg.h',
            'jpegint.h',
            'jpeglib.h',
            'jquant1.c',
            'jquant2.c',
            'jutils.c',
            'jversion.h',
          ],
          'include_dirs': [
            '<(DEPTH)',
            '.',
          ],
          'direct_dependent_settings': {
            'include_dirs': [
              '<(DEPTH)',
              '.',
            ],
          },
          'conditions': [
            ['OS!="win"', {'product_name': 'jpeg'}],
          ],
        },
      ],
    }, {
      'targets': [
        {
          'target_name': 'libjpeg',
          'type': 'none',
          'direct_dependent_settings': {
            'defines': [
              'USE_SYSTEM_LIBJPEG',
            ],
          },
          'link_settings': {
            'libraries': [
              '-ljpeg',
            ],
          },
        }
      ],
    }],
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
