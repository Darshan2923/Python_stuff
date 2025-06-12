import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Home } from './home/home';
import { Header } from './components/header/header';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, Home, Header],
  template: `
    <app-header></app-header>
    <main>

      <app-home></app-home>
    </main>
    <router-outlet>

  `,
  styles: [`
      // p{
      //   background-color:red;
      // }
      main{
        padding:8px
      }
    `],
})
export class App {
  protected title = 'first-ng-app';
}
