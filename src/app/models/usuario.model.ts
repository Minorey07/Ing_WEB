export interface Usuario {
  id?: string;
  nombre: string;
  correo: string;
  password: string;
  rol: 'ADMIN' | 'ALMACENERO' | 'VENDEDOR';
}