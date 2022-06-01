# Pages
__Domain: csup.app__

## Root (csup.app/)
- home 
- {legal stuff}

## Accounts (accounts/)
- logout
- discord/login
- discord/login/callback

## Messages (messages/)
- list

## Admin (admin/)
- predefined

## Drivers (driver/)
- list (show all drivers with links to profiles)
- {driver_id}/view (view someones - can be yours as well - profile) => csup.app/driver/3/view
- {driver_id}/edit (edit your profile)

## Teams (team/)
- list (see list of your teams)
- create (create a team)
- {team_id}/view (view team profile) => csup.app/team/2/view
- {team_id}/edit (edit your team)

## Events (events/)
- dashboard 
    - navibar 
        - Home
        - Leagues
        - Teams
        - Drivers
        - indication of new messages
    - some stats
    - next race
    - current leagues one organizes
    - current leagues one participates in


### League (league/)
- list (see all leagues)
- team/create => csup.app/events/league/team/create
- single/create => csup.app/events/league/single/create
- {league_id}/view => Standings
- {league_id}/edit (only organizers)

#### Applications ({league_id}/application/)
- create
- {application_id}/delete (only applicant) => csup.app/events/league/1/application/10/delete
- {application_id}/answer (only organizers)

#### Races ({league_id}/race/)
- list (everyone)
- create (only league organizers)
- {race_id}/view (everyone)
- {race_id}/edit (only league organizers)
- {race_id}/delete (only league organizers)

##### Results ({race_id}/result/)
- list/overview of race results with penalties (everyone)
- create (only league organizers)
- {result_id}/edit (only league organizers)
- {result_id}/delete (only league organizers)

###### Penalties ({result_id}/penalty/)
- create (only league organizers)
- {penalty_id}/edit (only league organizers)
- {penalty_id}/delete (only league organizers)