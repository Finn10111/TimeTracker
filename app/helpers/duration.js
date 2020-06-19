import { helper } from '@ember/component/helper';

export default helper(function duration(params/*, hash*/) {
  return (Math.floor((params / 3600)) % 3600).toString().padStart(2, '0') + ':' + 
    (Math.floor((params / 60)) % 60).toString().padStart(2, '0') + ':' + 
    (params % 60).toString().padStart(2, '0');
});
