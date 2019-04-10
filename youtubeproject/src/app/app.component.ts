import { Component } from '@angular/core';
import {DownloadService} from './service/download.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
   videoUrl: any;
 
  constructor(private _downloadService: DownloadService){
    
  }
 
 downloadVideo(){
   this._downloadService.downloadVideoService(this.videoUrl).subscribe((data)=>{
     

   });


 }


}