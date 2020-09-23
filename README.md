# Metro_Navigator_by_Landmarks
Landmark to Landmark navigation system using railways. In this project I will use a Map of the Vancouver Metro Station, and a corresponding list of landmarks with their near by train stations to give the optimal metro path from Landmark A to Landmark B.

I used BFS and DFS to traverse the Metro map for all paths a path from Location A to Location B then found the shortest path and present it to the user. 

This project also takes into consideration trainstations that may be closed and find a workaround to these obsticales. 


Sample Output:


      Hi there and welcome to SkyRoute!
      We'll help you find the shortest route between the following Vancouver landmarks:
      a - Marine Building
      b - Scotiabank Field at Nat Bailey Stadium
      c - Vancouver Aquarium
      d - Vancouver Lookout
      e - Canada Place
      f - Cathedral of Our Lady of the Holy Rosary
      g - Library Square
      h - B.C. Place Stadium
      i - Lions Gate Bridge
      j - Gastown Steam Clock
      k - Waterfront Station
      l - Granville Street
      m - Pacific Central Station
      n - Prospect Point Lighthouse
      o - Queen Elizabeth Theatre
      p - Stanley Park
      q - Granville Island Public Market
      r - Kitsilano Beach
      s - Dr. Sun Yat-Sen Classical Chinese Garden
      t - Museum of Vancouver
      u - Science World
      v - Robson Square
      w - Samson V Maritime Museum
      x - Burnaby Lake
      y - Nikkei National Museum & Cultural Centre
      z - Central Park


  Where are you coming from?
  Type in the corresponding letter: d

  Where are you heading to
  Type in the corresponding letter: t


      Your current path is

      FROM: Vancouver Lookout        
      TO: Museum of Vancouver        

      What would you like to change? 

      You can enter 'o' for 'origin',
      'd' for 'destination'
      'b' for 'both', or
      'n' for neiter.
      -> b

  Where are you coming from?
  Type in the corresponding letter: t

  Where are you heading to
  Type in the corresponding letter: u


      Your current path is

      FROM: Museum of Vancouver
      TO: Science World

      What would you like to change?

  You can enter 'o' for 'origin',
  'd' for 'destination'
  'b' for 'both', or
  'n' for neiter.
  -> n

      The shortest route from Museum of Vancouver to Science World:
      Yaletown-Roundhouse
      Vancouver City Centre
      Waterfront
      Burrard
      Granville
      Stadium-Chinatown
      Main Street-Science World

  Would you like to see another route? Enter y/n: y

      Route #0 from Museum of Vancouver to Science World:
      Yaletown-Roundhouse
      Vancouver City Centre
      Waterfront
      Burrard
      Granville
      Stadium-Chinatown
      Main Street-Science World

  Would you like to see another route? Enter y/n: y
  All possible routes have been printed. Would you like to restart to list of possible routes? Enter y/n n

      Thank you for using SkyRoute!
      Come Again!
          
-----END-----
          
          
          
          
          
          
Computer Science Capstone Project from Codecademy. Please feel free to give it a try :) Thank you for stoping by!
