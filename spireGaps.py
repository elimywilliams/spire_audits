#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs Dec 31 2020
@author: emilywilliams
"""
import geopandas as gpd
import pandas as pd


def getGapInfo(gap_df, polygon):
    i = 0
    if 'OBJECTID_1' in gap_df.columns:
        idloc = 'OBJECTID_1'
    elif 'OBJECTID_1' not in gap_df.columns:
        idloc = 'OBJECTID'
        
    if polygon == 'P8':
        idloc = 'OBJECTID'
    x = 0
    xportion = gap_df.reset_index()[idloc][x]

    if gap_df.reset_index().geometry[0].geom_type != "Polygon":
        g1x0, g1y0 = gap_df.reset_index().geometry[x][0].exterior.xy
        gapbuffinf = pd.DataFrame(
            {'lon': g1x0, 'lat': g1y0, 'POLYGON': polygon, 'portion': xportion, 'subportion': 1, 'multiple': True})

        g1x0, g1y0 = gap_df.reset_index().geometry[x][1].exterior.xy
        gap1temp = pd.DataFrame(
            {'lon': g1x0, 'lat': g1y0, 'POLYGON': polygon, 'portion': xportion, 'subportion': 2, 'multiple': True})
        gapbuffinf = gapbuffinf.append([gap1temp])
    elif gap_df.reset_index().geometry[0].geom_type == "Polygon":
        g1x0, g1y0 = gap_df.reset_index().geometry[0].exterior.xy
        gapbuffinf = pd.DataFrame(
            {'lon': g1x0, 'lat': g1y0, 'POLYGON': polygon, 'portion': xportion, 'subportion': 1, 'multiple': False})

    for x in range(2, int(gap_df.reset_index().shape[0]) + 1):
        # print(x)
        # print (gap_df.reset_index().geometry[x].geom_type)
        if gap_df.reset_index().geometry[x - 1].geom_type != "Polygon":
            # xportion = gap_df.reset_index().OBJECTID_1[x]
            xportion = gap_df.reset_index()[idloc][x - 1]
            # print(xportion)
            g1x0, g1y0 = gap_df.reset_index().geometry[x - 1][0].exterior.xy
            gap1temp = pd.DataFrame(
                {'lon': g1x0, 'lat': g1y0, 'POLYGON': polygon, 'portion': xportion, 'subportion': 1, 'multiple': True})
            gapbuffinf = gapbuffinf.append([gap1temp])

            g1x0, g1y0 = gap_df.reset_index().geometry[x - 1][1].exterior.xy
            gap1temp = pd.DataFrame(
                {'lon': g1x0, 'lat': g1y0, 'POLYGON': polygon, 'portion': xportion, 'subportion': 2, 'multiple': True})
            gapbuffinf = gapbuffinf.append([gap1temp])

        elif gap_df.reset_index().geometry[x - 1].geom_type == "Polygon":
            # print(type(gaps1buff.reset_index().geometry[x]))
            # print(gaps1buff.reset_index().FID_GAPS_2[x])
            xportion = gap_df.reset_index()[idloc][x - 1]

            g1x0, g1y0 = gap_df.reset_index().geometry[x - 1].exterior.xy
            gap1temp = pd.DataFrame(
                {'lon': g1x0, 'lat': g1y0, 'POLYGON': polygon, 'portion': xportion, 'subportion': 1, 'multiple': False})
            gapbuffinf = gapbuffinf.append([gap1temp])

    return (gapbuffinf)


gaps4 = gpd.read_file('/Users/emilywilliams/Documents/GitHub/spire_audits_corrected/Polygon4/Gaps_4.shp')
gap4info = getGapInfo(gaps4, 'P4')

gaps5 = gpd.read_file('/Users/emilywilliams/Documents/GitHub/spire_audits_corrected/Polygon5/Gaps_5.shp')
gap5info = getGapInfo(gaps5, 'P5')

gaps6 = gpd.read_file('/Users/emilywilliams/Documents/GitHub/spire_audits_corrected/Polygon6/Gaps_6.shp')
gap6info = getGapInfo(gaps6, 'P6')

gaps7 = gpd.read_file('/Users/emilywilliams/Documents/GitHub/spire_audits_corrected/Polygon7/Gaps_7.shp')
gap7info = getGapInfo(gaps7, 'P7')

gaps8 = gpd.read_file('/Users/emilywilliams/Documents/GitHub/spire_audits_corrected/Polygon8/Gaps_8.shp')
gap8info = getGapInfo(gaps8, 'P8')


#gapsTogether = gap1info.append(
#    [gap2info, gap3info, gap4info, gap5info, gap7info, gap8info, gap10info, gap11info, gap58info, gap59info, gap22info])
gapsTogether = gap4info.append([gap5info,gap6info,gap7info,gap8info])

gapsTogether.to_csv('/Users/emilywilliams/Documents/GitHub/spire_audits/allGaps.csv')

