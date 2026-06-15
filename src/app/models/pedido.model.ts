import { PedidoDetalle } from "./PedidoDetalle.model";

export interface Pedido {
  id: number;
  clienteId: number;
  vendedorId: number;
  fecha: Date;
  estado: 'PENDIENTE' | 'ENTREGADO';

  detalles: PedidoDetalle[];

  total: number;
}