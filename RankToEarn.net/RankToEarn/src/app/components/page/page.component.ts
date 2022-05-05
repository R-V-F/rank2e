import { AfterViewInit, Component, Input, OnInit, Output, EventEmitter, OnDestroy } from '@angular/core';

import datajson from './json_data_appended.json';
import { ActivatedRoute, Router, RoutesRecognized } from '@angular/router';
import Chart from 'chart.js/auto';
import { Subscription } from 'rxjs';
import { SetIdService } from 'src/app/service/set-id.service';
import { GetRanksService } from 'src/app/service/get-ranks.service';

@Component({
  selector: 'app-page',
  templateUrl: './page.component.html',
  styleUrls: ['./page.component.css']
})
export class PageComponent implements OnInit, AfterViewInit, OnDestroy {

  id:number;
  project_name:string;
  opt:number;
  thumbnail_path:string;
  @Input() input_id:number;
  position:number;
  subscription:Subscription;
  plugged_Discord:any;
  plugged_Twitter:any;
  aux_set:any[];
  socials:any;
  name:string;

  grade_array_4 = [0,0,0,0];
  grade_array_5 = [0,0,0,0,0];
  
  disc_rank:any;
  disc_growth_rank:any;
  twitter_rank:any;
  twitter_growth_rank:any;

  rank_discord_returns:any[];
  rank_twitter_returns:any[];

  constructor(
    private route:ActivatedRoute,
    private router: Router,
    public service_id:SetIdService,
    private get_ranks:GetRanksService
    ) { 
    console.log('page comp * constructor call');
    this.subscription = service_id.getUser().subscribe(id_next => {
      this.id = id_next;
      console.log('page comp * received id_next:', id_next);

      this.rank_discord_returns = get_ranks.getRankDiscord(this.id);
      // for(let i = 0; i < this.rank_discord_returns.length; i++) console.log('page stats',this.rank_discord_returns[i]);
      this.rank_twitter_returns = get_ranks.getRankTwitter(this.id);
      // for(let i = 0; i < this.rank_discord_returns.length; i++) console.log('page stats',this.rank_twitter_returns[i]);\
      this.name = get_ranks.getName();

    });


    



    }

  ngOnInit(): void {
  
  
    for(let i = 0; i < datajson.tables.length; i++) {
      if(datajson.tables[i].id == this.id) {
        this.position = i;
        break;
      }
    }
  
    if(!(typeof this.id === 'undefined')) {
      if(this.plugged_Discord && this.plugged_Twitter) {
        this.plugged_Discord.destroy();
        this.plugged_Twitter.destroy();
        this.plugged_Discord = this.plugDiscord(datajson.tables[this.position]);
        this.plugged_Twitter = this.plugTwitter(datajson.tables[this.position]);
      }
      else {
        this.plugged_Discord = this.plugDiscord(datajson.tables[this.position]);
        this.plugged_Twitter = this.plugTwitter(datajson.tables[this.position]);
      }
    }
    else {
      console.log('page comp * table not found!');
    }

    this.socials = datajson.tables[this.position].socials;




  }

  ngAfterViewInit(): void {
    
  }

  ngOnDestroy(): void {
    console.log('page comp * ngOnDestroy destroying things crazy life');
    if(typeof this.plugged_Discord != 'number') this.plugged_Discord.destroy();
    if(typeof this.plugged_Twitter != 'number')this.plugged_Twitter.destroy();
    this.subscription.unsubscribe();
  }


  make_chart_arg(type:string, name:string, dates_discord:string[], size_discord:any[] , dates_twitter:string[], size_twitter:any[]){
    let bigger_dates_set;
    let discord_label = name + ' Discord';
    let twitter_label = name + ' Twitter';
    let Charts:Chart[];
    let myChart_Discord:Chart;
    let myChart_Twitter:Chart;
    console.log('Verifying:', dates_discord.length, dates_twitter.length);

    if(type == 'myDiscordCanvas' && size_discord[size_discord.length-1] > 0) {

      myChart_Discord = new Chart('myDiscordCanvas', {
        
        type: 'line',
        data: {
          labels: dates_discord,
          datasets: [{

            label: discord_label,
            data: size_discord,
            pointRadius: 0,
            backgroundColor: 
              '#8292ea',
            borderColor:
              '#8292ea',
            borderWidth: 2.5,
            tension: 0.25

            }],
        },
        options: {
            scales: {
                x: {
                  ticks: {
                    display:true
                  },
                  grid: {
                    display:false
                  }
                },
                y: {
                  beginAtZero:false
                }
            }
          
        }
      });
      return myChart_Discord;
    }

    else if(type == 'myTwitterCanvas' && size_twitter[size_twitter.length-1] > 0) {

      myChart_Twitter = new Chart('myTwitterCanvas', {
        
        type: 'line',
        data: {
          labels: dates_twitter,
          datasets: [{
            
            label: twitter_label,
            data: size_twitter,
            pointRadius: 0,
            backgroundColor: 
              '#33ccff',
            
            borderColor:
              '#33ccff',
              
            borderWidth: 2.5,
            fill:false,
            tension: 0.25
            
            }],
        },
        options: {
            scales: {
                x: {
                  ticks: {
                    display:true
                  },
                  grid: {
                    display:false
                  } 
                },
                y: {
                  beginAtZero:false
                }
            }
        }
      });
      return myChart_Twitter;
    }
    else {

      return 0;
    }
    
  }

  plugDiscord(table:any) {
    
    try{
      this.thumbnail_path = table.img_path;
      console.log(table.img_path);
    }
    catch(e){
      console.log(e);
    }

    this.project_name = table.name;

    return this.make_chart_arg('myDiscordCanvas',table.name, table.dates, table.members, table.twt_dates, table.followers);

  }
  plugTwitter(table:any) {
    
    try{
      this.thumbnail_path = table.img_path;
      console.log(table.img_path);
    }
    catch(e){
      console.log(e);
    }

    this.project_name = table.name;

    return this.make_chart_arg('myTwitterCanvas',table.name, table.dates, table.members, table.twt_dates, table.followers);
  }


  backToMain() {
    this.router.navigate([''],{
      queryParams: {'page': 1},
      queryParamsHandling: 'merge'

    
  });




  }




}
