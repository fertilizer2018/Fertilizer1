import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";


@Component({
  selector: 'app-register-comp',
  templateUrl: './register-comp.component.html',
  styleUrls: ['./register-comp.component.scss']
})
export class RegisterCompComponent implements OnInit {

  constructor(private http:HttpClient) { }

  ngOnInit() {
  }


  register(){
    console.log("register call ");
    this.http.post("http://127.0.0.1:8000/shoper/student2/",{
      "name":"abc",
      "lastName":"XYZ",
      "email":"xyz@gmail.com"
      }).subscribe(data =>{
        console.log("POST DATA : "+JSON.stringify(data));
      },
        error1 => {
          console.log("Eroor post DATA : ");
        }
    );
  }

}
