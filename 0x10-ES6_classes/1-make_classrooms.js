import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const c19 = new ClassRoom(19);
  const c20 = new ClassRoom(20);
  const c34 = new ClassRoom(34);
  return [c19, c20, c34];
}
