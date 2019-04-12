import { Component } from '@angular/core';
import {DownloadService} from './service/download.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
   videoUrl: any;
   status:any;
  constructor(private _downloadService: DownloadService){ 
  }
  searchVideos() {
   this._downloadService.searchVideosService(this.videoUrl).subscribe((data) => {

    this.status = data;
    if (this.status.status === true) {
     
    } else {
      Swal.fire(
        'Error',
        'Please check the URL ! ',
        'error'
      );
    }
   });
 }
 clearURL() {
   this.videoUrl = '';
 }




}