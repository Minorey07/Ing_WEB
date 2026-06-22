import { PedidoDetalle } from "./PedidoDetalle.model";

export interface Pedido {
  id: number;
  clienteId: number;
  vendedorId: number;
  fecha: Date;
  estadoId: number;
  estadoNombre?: string;
  clienteNombre?: string;
  vendedorNombre?: string;

  detalles: PedidoDetalle[];

  total: number;
}