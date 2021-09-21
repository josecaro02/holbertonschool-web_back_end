export default function getListStudentIds(listObject) {
  if (!Array.isArray(listObject)) return [];
  return listObject.map((item) => item.id);
}
