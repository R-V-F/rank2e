import { Injectable, OnInit } from '@angular/core';
import datajson from './json_data_appended_and_sorted.json';


@Injectable({
  providedIn: 'root'
})
export class GetRanksService {

  //[[1,2],[2,3]]
  public discord_list:any[];
  public twitter_list:any[];
  public member_id:any[];
  public followers_id:any[];

  name:string;

  discord_rank:number;
  twitter_rank:number;
  
  constructor() {
    
  }




  /* 
  * 
  * return format: 
  * 
  * return [(rank), (7d), (30d)]
  * 
  */

  getRankDiscord(id:number){
    this.member_id = new Array();
    this.discord_list = new Array();
    let discord_return_array = new Array();
    let pos = 0;
    
    for(let i = 0; i < datajson.tables.length; i++) {
      if(datajson.tables[i].id == id){
        pos = i;
        this.name = datajson.tables[pos].name;
      }
      this.member_id[0] = (datajson.tables[i].members[datajson.tables[i].members.length-1]);
      this.member_id[1] = (datajson.tables[i].id);
      this.discord_list.push(this.member_id.splice(0,2));
    } //[[s1,id1],[s2,id2],[s3,id3]...]

    let i=1,j=0;
    for(i;i < this.discord_list.length; i++) {
      for (j = 0; j < this.discord_list.length - i; j++){
        if(this.discord_list[j][0] < this.discord_list[j+1][0]) {
          let aux = this.discord_list[j];

          this.discord_list[j] = this.discord_list[j+1];
          
          this.discord_list[j+1] = aux;

        }
      }
    }//sorted dsc

    let rank = 1;
    let flag = 0;
    for(let i = 0; i < this.discord_list.length; i++) {
      if(this.discord_list[i][1] == id) {
        
        flag = 1;
        if(this.discord_list[i][0] <= 0) {
          
          //return -1; //In case the members count <= 0
          discord_return_array.push(-1);
          break;
        } 
        this.discord_rank = rank;
        discord_return_array.push(rank);
        break;
        //return rank;
      }
      rank++;
    }
    if(flag == 0) discord_return_array.push(-2);
    //return -2; //In case no match was found

    
    if(datajson.tables[pos].members[(datajson.tables[pos].members.length)-1] != 0 && datajson.tables[pos].members[(datajson.tables[pos].members.length)-8] != 0 && datajson.tables[pos].members.length > 6) {
      let ratio = (datajson.tables[pos].members[(datajson.tables[pos].members.length)-1]) / (datajson.tables[pos].members[(datajson.tables[pos].members.length)-8]);
      ratio = (ratio-1)*100;
      ratio = Math.round(ratio * 100) / 100;
      discord_return_array.push(ratio);
    }
    else {
      discord_return_array.push(-99);
    }


    if(datajson.tables[pos].members[(datajson.tables[pos].members.length)-1] != 0 && datajson.tables[pos].members[(datajson.tables[pos].members.length)-31] != 0 && datajson.tables[pos].members.length > 30) {
      let ratio = (datajson.tables[pos].members[(datajson.tables[pos].members.length)-1]) / (datajson.tables[pos].members[(datajson.tables[pos].members.length)-31]);
      ratio = (ratio-1)*100;
      ratio = Math.round(ratio * 100) / 100;
      discord_return_array.push(ratio);
    }
    else {
      discord_return_array.push(-99);
    }


    return discord_return_array;



  }

  getRankTwitter(id:number){
    this.followers_id = new Array();
    this.twitter_list = new Array();
    let pos = 0;
    let twitter_return_array = new Array(); // [(rank),(7d),(30d)]

    
    for(let i = 0; i < datajson.tables.length; i++) {
      if(datajson.tables[i].id == id){
        pos = i;
        this.name = datajson.tables[pos].name;
      }
      this.followers_id[0] = (datajson.tables[i].followers[datajson.tables[i].followers.length-1]);
      this.followers_id[1] = (datajson.tables[i].id);
      this.twitter_list.push(this.followers_id.splice(0,2));
    } //[[s1,id1],[s2,id2],[s3,id3]...]

    let i=1,j=0;
    for(i;i < this.twitter_list.length; i++) {
      for (j = 0; j < this.twitter_list.length - i; j++){
        if(this.twitter_list[j][0] < this.twitter_list[j+1][0]) {
          let aux = this.twitter_list[j];

          this.twitter_list[j] = this.twitter_list[j+1];
          
          this.twitter_list[j+1] = aux;

        }
      }
    }//sorted dsc

    let rank = 1;
    let flag = 0;
    for(let i = 0; i < this.twitter_list.length; i++) {
      if(this.twitter_list[i][1] == id) {
        flag = 1;
        if(this.twitter_list[i][0] <= 0) {
          //return -1; //In case the members count <= 0
          twitter_return_array.push(-1);
          break;
        } 
        twitter_return_array.push(rank);
        //return rank;
        break;
      }
      rank++;
    }
    if(flag == 0) twitter_return_array.push(-2);; //In case no match was found

    if(datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-1] != 0 && datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-8] != 0 && datajson.tables[pos].followers.length > 6) {
      let ratio = (datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-1]) / (datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-8]);
      ratio = (ratio-1)*100;
      ratio = Math.round(ratio * 100) / 100;
      twitter_return_array.push(ratio);
    }
    else {
      twitter_return_array.push(-99);
    }

    if(datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-1] != 0 && datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-31] != 0 && datajson.tables[pos].followers.length > 29) {
      let ratio = (datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-1]) / (datajson.tables[pos].followers[(datajson.tables[pos].followers.length)-31]);
      ratio = (ratio-1)*100;
      ratio = Math.round(ratio * 100) / 100;
      twitter_return_array.push(ratio);
    }
    else {
      twitter_return_array.push(-99);
    }

    return twitter_return_array;
  }

  getName() {
    return this.name;
  }

}




