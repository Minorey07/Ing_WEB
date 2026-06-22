export interface Usuario {
  id?: number;
  nombre: string;
  correo: string;
  password: string;
  rolId: number;
  rolNombre?: string;
}