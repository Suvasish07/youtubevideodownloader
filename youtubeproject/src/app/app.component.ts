import { Component } from '@angular/core';
import {DownloadService} from './service/download.service';
import Swal from 'sweetalert2';
import { DOCUMENT } from '@angular/common';
import * as $ from 'jquery'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
   videoUrl: any;
   videoUrlDetails:any;
   videoDetailsArr:any=[]
  constructor(private _downloadService: DownloadService){ 
  }
  searchVideos() {
   document.getElementById("loader").style.display = "block";
   document.getElementById("videolist").style.display = "none";

   this._downloadService.searchVideosService(this.videoUrl).subscribe((data) => {

    this.videoUrlDetails = data;
    if (this.videoUrlDetails.status === true) {
    
     this.videoDetailsArr=this.videoUrlDetails.data
     document.getElementById("loader").style.display = "none";
     document.getElementById("videolist").style.display = "block";
     $('html,body').animate({
      scrollTop: $(".videodiv").offset().top},
      'slow');
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