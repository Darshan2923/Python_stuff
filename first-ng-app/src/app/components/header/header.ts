import { Component, signal } from '@angular/core';
import { RouterLink } from '@angular/router';
// import { Todos } from '../../services/todos';

@Component({
  selector: 'app-header',
  imports: [RouterLink],
  templateUrl: './header.html',
  styleUrl: './header.scss',
  // providers: [Todos],
})
export class Header {
  title = signal('My first Angular App');
}
