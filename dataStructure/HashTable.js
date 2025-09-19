class HashTable {
  constructor(size = 1) {
    this.keyMap = new Array(size);
  }

  _hash(key) {
    let total = 0;
    let WEIRD_PRIME = 31;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      let char = key[i];
      let value = char.charCodeAt(0) - 96;
      total = (total * WEIRD_PRIME + value) % this.keyMap.length;
    }
    return total;
  }

  set(key, val) {
    const hashIndex = this._hash(key);
    if (!this.keyMap[hashIndex]) {
      this.keyMap[hashIndex] = [];
    } else if (this.get(key)) {
      for (const keyValue of this.keyMap[hashIndex]) {
        if (keyValue.key === key) keyValue.val = val;
      }
    }
    if (!this.get(key)) {
      console.log(this.get(key));
      this.keyMap[hashIndex].push({ key, val });
    }
  }

  get(key) {
    const hashIndex = this._hash(key);
    if (this.keyMap[hashIndex]) {
      for (const keyValue of this.keyMap[hashIndex]) {
        if (keyValue.key === key) return keyValue.val;
      }
    }
    return undefined;
  }

  keys() {
    const keys = new Set();
    for (const keyValue of this.keyMap) {
      if (keyValue) {
        keyValue.forEach((keyValue) => {
          keys.add(keyValue.key);
        });
      }
    }
    return Array.from(keys);
  }

  values() {
    const values = new Set();
    for (const keyValue of this.keyMap) {
      if (keyValue) {
        keyValue.forEach((keyValue) => {
          values.add(keyValue.val);
        });
      }
    }
    return Array.from(values);
  }
}

const map = new HashTable();
map.set("test", 56);
map.set("test1", 55);
console.log(map.keyMap);
console.log(map.keys());
console.log(map.values());
