export interface Producto {
  id: number;
  nombre: string;
  descripcion: string;
  precio: number;
  stock: number;
  estadoId: number;
  estadoNombre?: string;
  categoriaId?: number;
  categoriaNombre?: string;
}