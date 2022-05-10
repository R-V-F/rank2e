import { AfterViewInit, Component, Input, OnInit, Output, EventEmitter, OnDestroy } from '@angular/core';

import datajson from './json_data_appended_and_sorted.json';
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
export class PageComponent implements OnInit, OnDestroy {

  
  /** Used to get the id from route */

  subscription:Subscription;

  /** Used to handle the Charts */

  plugged_Discord:any;
  plugged_Twitter:any;

  /** General project properties */

  socials:any;
  name:string;
  img_array = ['none'];
  id:number;
  project_name:string;
  thumbnail_path:string;
  position:number;

  /** Whacky placehodler for growth/engagement scores */

  grade_array_4:any = [0,0,0,0];
  grade_array_5:any = [0,0,0,0,0];
  
  /** Receivers of get-ranks.service */

  rank_discord_returns:any[];
  rank_twitter_returns:any[];

  /** Index for the main gallery photo */

  ind_center:number;

  /** Appended info */

  blockchains:string;
  devices:string;
  genres:string;


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
      //console.log('rank_twitter_returns[2]:', this.rank_twitter_returns[2]);
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

    this.blockchains = datajson.tables[this.position].blockchains;
    this.devices = datajson.tables[this.position].devices;
    this.genres = datajson.tables[this.position].genres;
  
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
    
    
    this.plugGallery(this.position);
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

  plugGallery(position:number) {
    let folder_path = "\\assets\\img\\" + datajson.tables[position].name;
    let check = true;
    let i = 0;
    var xhr = new XMLHttpRequest();
    this.img_array.pop();
    

    while(check == true) {
      let img_path = folder_path + "\\" + i.toString() + ".png";
      xhr.open('HEAD', img_path, false);
      xhr.send();
      if (xhr.status == 404) {
          console.log('no photo in this path:',img_path);
          break;
      } else {
          console.log('web_page found');
          this.img_array.push(img_path);
      }  
      i++;
    }
    xhr.open('HEAD', folder_path + "\\web_page.png", false);
    xhr.send();
     
    if (xhr.status == 404) {
        console.log('no web_page');
    } else {
        console.log('web_page found:', folder_path + "\\web_page.png");
        console.log(this.img_array);
        this.img_array.push(folder_path + "\\web_page.png");
    }

    console.log('checking img_array:',this.img_array);
    this.ind_center = 0;
    // this.ind_left = this.img_array.length - 1;
    // this.ind_right = 1;



  }
  changePhoto(side:number) {
    if(side == -1 && this.ind_center == 0) {
      this.ind_center = this.img_array.length-1;
    }
    else {
      // this.ind_left = (this.ind_left+side) % this.img_array.length;
      // this.ind_right =  (this.ind_right+side) % this.img_array.length;
      this.ind_center = (this.ind_center+side) % this.img_array.length;
    }
    //console.log(this.img_array[this.ind_center]);
  }
  

}

