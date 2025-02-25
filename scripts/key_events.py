import pandas as pd
import matplotlib.pyplot as plt

EVENTS_DATA = {
  'Date': [
    # 1987–1996 (20 events)
    '1987-07-01', '1988-07-18', '1989-02-15', '1989-12-20', '1990-08-02',
    '1990-10-01', '1991-01-17', '1991-03-01', '1991-06-01', '1992-06-01',
    '1993-03-01', '1994-03-01', '1994-11-01', '1995-03-01', '1995-06-01',
    '1996-03-01', '1996-06-01', '1996-09-01', '1996-11-01', '1996-12-01',
    # 1997–2006 (30 events)
    '1997-03-01', '1997-06-25', '1997-11-01', '1998-03-25', '1998-06-24',
    '1998-12-01', '1999-03-23', '1999-06-01', '2000-03-28', '2000-06-21',
    '2000-09-01', '2001-01-17', '2001-09-11', '2002-01-01', '2002-06-26',
    '2003-01-12', '2003-03-20', '2003-06-01', '2004-05-01', '2004-08-01',
    '2005-01-30', '2005-06-15', '2005-08-29', '2005-12-12', '2006-03-08',
    '2006-07-12', '2006-10-19', '2006-12-14', '2007-03-01', '2007-06-01',
    # 2007–2016 (30 events)
    '2007-09-11', '2007-12-05', '2008-03-05', '2008-07-11', '2008-09-15',
    '2008-10-24', '2008-12-17', '2009-03-01', '2009-05-28', '2010-04-20',
    '2010-10-14', '2011-02-15', '2011-06-08', '2011-12-14', '2012-03-01',
    '2012-07-01', '2013-03-01', '2013-07-01', '2014-03-01', '2014-06-01',
    '2014-11-27', '2015-06-05', '2015-12-04', '2015-12-18', '2016-04-17',
    '2016-09-28', '2016-11-30', '2017-03-01', '2017-05-25', '2017-06-01',
    # 2017–2022 (20 events)
    '2017-11-30', '2018-05-08', '2018-06-22', '2018-11-05', '2018-12-07',
    '2019-03-01', '2019-07-02', '2019-12-05', '2020-01-03', '2020-03-06',
    '2020-03-11', '2020-04-12', '2020-06-06', '2020-12-03', '2021-03-04',
    '2021-07-18', '2021-10-04', '2022-02-24', '2022-06-02', '2022-09-05'
  ],
  'Event_Type': [
    # 1987–1996
    'OPEC Policy', 'Conflict Resolution', 'Sanctions', 'Political Decision', 'Conflict',
    'Sanctions', 'Conflict', 'Conflict Resolution', 'OPEC Policy', 'OPEC Policy',
    'Sanctions', 'Sanctions', 'OPEC Policy', 'Political Decision', 'OPEC Policy',
    'Sanctions', 'OPEC Policy', 'Political Decision', 'OPEC Policy', 'Sanctions',
    # 1997–2006
    'OPEC Policy', 'OPEC Policy', 'Sanctions', 'OPEC Policy', 'OPEC Policy',
    'OPEC Policy', 'OPEC Policy', 'Political Decision', 'OPEC Policy', 'OPEC Policy',
    'Sanctions', 'OPEC Policy', 'Conflict', 'OPEC Policy', 'OPEC Policy',
    'OPEC Policy', 'Conflict', 'Political Decision', 'Sanctions', 'Political Decision',
    'OPEC Policy', 'OPEC Policy', 'Political Decision', 'OPEC Policy', 'Sanctions',
    'Conflict', 'OPEC Policy', 'OPEC Policy', 'Sanctions', 'Political Decision',
    # 2007–2016
    'OPEC Policy', 'OPEC Policy', 'Sanctions', 'Economic', 'Economic',
    'OPEC Policy', 'OPEC Policy', 'OPEC Policy', 'Political Decision', 'Political Decision',
    'OPEC Policy', 'Conflict', 'OPEC Policy', 'OPEC Policy', 'Sanctions',
    'Sanctions', 'Political Decision', 'Conflict', 'Sanctions', 'Sanctions',
    'OPEC Policy', 'OPEC Policy', 'OPEC Policy', 'Political Decision', 'OPEC Policy',
    'OPEC Policy', 'OPEC Policy', 'Sanctions', 'OPEC Policy', 'Political Decision',
    # 2017–2022
    'OPEC Policy', 'Sanctions', 'OPEC Policy', 'Sanctions', 'OPEC Policy',
    'Sanctions', 'OPEC Policy', 'OPEC Policy', 'Conflict', 'OPEC Policy',
    'Economic', 'OPEC Policy', 'OPEC Policy', 'OPEC Policy', 'OPEC Policy',
    'OPEC Policy', 'OPEC Policy', 'Conflict', 'OPEC Policy', 'War'
  ],
  'Event_Description': [
    # 1987–1996
    'OPEC stabilizes prices post-1986 glut with quota enforcement',
    'Iran-Iraq War ends; oil supply stabilizes',
    'U.S. sanctions on Libya tightened',
    'U.S. Strategic Petroleum Reserve release announced',
    'Iraq invades Kuwait; Gulf War begins, oil supply fears spike',
    'UN sanctions imposed on Iraq post-invasion',
    'Gulf War air campaign begins; oil prices surge',
    'Gulf War ends; Iraqi oil supply resumes gradually',
    'OPEC increases production quotas post-Gulf War',
    'OPEC adjusts quotas to stabilize market',
    'UN extends Iraq sanctions, oil exports limited',
    'UN tightens sanctions on Iraq, limiting oil exports',
    'OPEC cuts production to support prices',
    'U.S. energy policy shifts favor domestic production',
    'OPEC increases output to meet demand',
    'UN imposes sanctions on Libya over Lockerbie',
    'OPEC adjusts quotas amid stable prices',
    'U.S. relaxes some oil import policies',
    'OPEC maintains production levels',
    'UN sanctions on Iraq persist, oil supply constrained',
    # 1997–2006
    'OPEC increases production quotas',
    'OPEC cuts production to counter low prices',
    'UN sanctions on Iraq adjusted under Oil-for-Food',
    'OPEC cuts production amid Asian financial crisis',
    'OPEC agrees to further cuts amid low prices',
    'OPEC boosts production to stabilize prices',
    'OPEC raises output to meet demand',
    'U.S. energy policy encourages shale development',
    'OPEC increases production quotas',
    'OPEC boosts output amid high prices',
    'U.S. sanctions on Iran tightened',
    'OPEC cuts production to stabilize prices',
    '9/11 attacks; oil prices spike due to uncertainty',
    'OPEC increases output to calm markets',
    'OPEC adjusts quotas to balance supply',
    'OPEC cuts production amid Iraq tensions',
    'U.S. invades Iraq; fears of oil supply disruption',
    'Iraq oil production resumes post-war',
    'UN lifts Iraq sanctions, oil exports rise',
    'U.S. energy policy shifts post-Iraq',
    'OPEC increases quotas amid high demand',
    'OPEC cuts production to support prices',
    'Hurricane Katrina disrupts U.S. Gulf oil production',
    'OPEC maintains output despite high prices',
    'U.S. imposes sanctions on Iran nuclear program',
    'Israel-Hezbollah War; Middle East tensions rise',
    'OPEC cuts production by 1 million bpd',
    'OPEC reduces output to counter oversupply',
    'UN sanctions on Iran escalate',
    'U.S. energy policy boosts biofuels',
    # 2007–2016
    'OPEC increases production quotas',
    'OPEC maintains output amid high prices',
    'U.S. sanctions on Iran tightened further',
    'Global financial crisis peaks; oil hits $147 then crashes',
    'Lehman Brothers collapse; oil demand plummets',
    'OPEC cuts production by 2.2 million bpd',
    'OPEC cuts production by 4.2 million bpd to counter crisis',
    'OPEC maintains output as prices recover',
    'U.S. energy policy shifts toward renewables',
    'Deepwater Horizon spill; U.S. Gulf production halted',
    'OPEC adjusts quotas amid recovery',
    'Arab Spring begins; Libyan oil production halted',
    'OPEC fails to reach production agreement',
    'OPEC maintains output amid Libyan recovery',
    'U.S. sanctions on Iran escalate',
    'EU sanctions on Iran over nuclear program begin',
    'U.S. energy policy boosts shale production',
    'Egypt unrest escalates; oil transit fears',
    'U.S. imposes new sanctions on Russia',
    'Russia annexes Crimea; Western sanctions imposed',
    'OPEC maintains output despite oversupply; prices crash',
    'OPEC maintains high production levels',
    'OPEC fails to cut production; prices drop',
    'U.S. lifts crude oil export ban, boosting supply',
    'OPEC+ Doha talks fail; no production freeze',
    'OPEC agrees to modest production cut in Algiers',
    'OPEC agrees to cut 1.2 million bpd; prices rise',
    'Iran sanctions eased under nuclear deal',
    'OPEC extends production cuts',
    'U.S. energy policy shifts under Trump',
    # 2017–2022
    'OPEC extends production cuts again',
    'U.S. withdraws from Iran nuclear deal; sanctions loom',
    'OPEC increases production to offset Iran losses',
    'U.S. reimposes sanctions on Iran; oil supply tightens',
    'OPEC+ agrees to cut production by 1.2 million bpd',
    'U.S. sanctions on Venezuela escalate',
    'OPEC+ extends production cuts',
    'OPEC+ agrees to further cuts amid demand fears',
    'U.S. drone strike kills Iran’s Soleimani; oil spikes',
    'OPEC+ talks fail; Saudi-Russia price war begins',
    'COVID-19 declared pandemic; oil demand collapses',
    'OPEC+ agrees to historic 9.7 million bpd cut',
    'OPEC+ extends deep cuts to July',
    'OPEC+ begins phasing out cuts',
    'OPEC+ increases output amid recovery',
    'OPEC+ agrees to gradual production increase',
    'OPEC+ boosts output as prices rise',
    'Russia invades Ukraine; oil prices surge due to supply fears',
    'OPEC+ increases production amid high prices',
    'Russia-Ukraine war, energy crisis'
  ]
}

def create_events_data(output_path):
  """
  Create a DataFrame of key events affecting Brent oil prices from 1987 to 2022 and save it to CSV.
  
  :param output_path: Directory to save the events CSV file.
  :return: DataFrame with events data.
  """
  events = pd.DataFrame(EVENTS_DATA)
  events['Date'] = pd.to_datetime(events['Date'])

  # Save to CSV
  events.to_csv(output_path, index=False)
  print(f"Events saved to '{output_path}'")

  return events
