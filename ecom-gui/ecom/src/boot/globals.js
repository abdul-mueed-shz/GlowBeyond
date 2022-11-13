let $router = null;
let $store = null;
export default ({ router, store }) => {
  $router = router;
  $store = store;
};

export function useGlobalRouter() {
  return $router;
}
export function useGlobalStore() {
  return $store;
}
